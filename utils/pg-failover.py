#!/usr/bin/python

from __future__ import print_function
import argparse
import datetime
import re
import socket

from fabric.api import task, run, sudo, execute, cd
from fabric.colors import blue, green, red, yellow
from fabric.utils import abort, error, puts
from fabric.contrib.console import confirm

parser = argparse.ArgumentParser(description="Perform a PostgreSQL primary server failover")
parser.add_argument("vip", metavar="VIP", help="The VIP address")
parser.add_argument("old", metavar="OLD", help="The old (current) primary server")
parser.add_argument("new", metavar="NEW", help="The new primary server")
parser.add_argument("-l", "--lb-server", metavar="HOST", action="append",
        help="Stop load balancer on this host during the failover")
parser.add_argument("-d", "--enable-idrac", action="store_true",
        help="Enable iDRAC remote access if it's not")
args = parser.parse_args()

try:
    vip = socket.gethostbyaddr(args.vip)
except socket.error as e:
    abort("Invalid VIP: " + args.vip + " - " + e.strerror)
vip_host = vip[0]
if not vip_host.startswith("v-") or not vip_host.endswith(".wumii.net"):
    abort("Invalid VIP host: {}".format(vip))
vip_ip = vip[2][0]

old_primary = args.old
new_primary = args.new

lb_servers = args.lb_server

def single_execute(host, task, *args, **kwargs):
    return execute(task, *args, host=host, **kwargs)[host]

def info(text):
    print(yellow(text))

def progress(text):
    print(blue("{} - {}".format(datetime.datetime.now(), text)))

# Ensure iDRAC remote access in case the server becomes inaccessible
@task
def enable_idrac_remote_access():
    sudo("/opt/wumii/bin/idrac-remote-access enable")

@task
def check_old_primary():
    sudo("/opt/wumii/bin/pg-failover-helper check_old_primary " + vip_ip, user="postgres")

@task
def check_new_primary():
    sudo("/opt/wumii/bin/pg-failover-helper check_new_primary " + vip_host, user="postgres")

@task
def control_apache(action):
    sudo("service apache " + action)

@task
def stop_old_primary():
    sudo("/opt/wumii/bin/pg-failover-helper stop_old_primary " + vip_ip)

@task
def start_new_primary():
    sudo("/opt/wumii/bin/pg-failover-helper start_new_primary " + vip_host + " " + vip_ip)

@task
def make_old_primary_standby():
    sudo("/opt/wumii/bin/pg-failover-helper make_old_primary_standby", user="postgres")


progress("Running sanity checks")
if args.enable_idrac:
    execute(enable_idrac_remote_access, hosts=[old_primary, new_primary])
execute(check_old_primary, host=old_primary)
execute(check_new_primary, host=new_primary)

if not confirm(green("Proceed to failover?"), default=False):
    abort("Aborting failover at user request")

if lb_servers:
    progress("Stopping load balancer(s)")
    execute(control_apache, "stop", hosts=lb_servers)

# Under normal circumstances, we can just shut down the primary (in smart or fast mode) and rest assured that all the standbys have received all WAL records.
#
# https://wiki.postgresql.org/wiki/Streaming_Replication
# "When smart/fast shutdown is requested, the primary waits to exit until XLOG records have been sent to the standby, up to the shutdown checkpoint record."
#
# http://www.postgresql.org/docs/current/static/warm-standby.html
# "as when using asynchronous replication, the server will not fully shutdown until all outstanding WAL records are transferred to the currently connected standby servers."
#
# Also https://phabricator.wumii.net/rPG985bd7d49726c9f178558491d31a570d47340459
progress("Stopping the old primary")
execute(stop_old_primary, host=old_primary)
progress("Starting the new primary")
execute(start_new_primary, host=new_primary)

if lb_servers:
    progress("Starting load balancer(s)")
    execute(control_apache, "start", hosts=lb_servers)
progress("Failover is successful")

execute(make_old_primary_standby, host=old_primary)
