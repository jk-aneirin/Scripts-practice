#!/usr/bin/env python
import SimpleHTTPServer
import SocketServer
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import ldap
import base64
import getpass

class ReferLdap():
    def __init__(self,ldap_server="ldaps://ldapserver:port"):
        self.ldap_server=ldap_server
        ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_ALLOW)
        self.ldapconn=ldap.initialize(self.ldap_server)
        self.authSF=False

    def ldapauth(self,username,password):
        user_dn="uid={},cn=users,cn=accounts,dc=example,dc=com".format(username)
        try:
            self.ldapconn.simple_bind_s(user_dn,password)
            self.authSF=True
        except ldap.LDAPError,e:
            print e
        finally:
            self.ldapconn.unbind_s()

class Handler(BaseHTTPRequestHandler):
    ''' Main class to present webpages and authentication. '''
    def do_HEAD(self):
        print "send header"
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_AUTHHEAD(self):
        print "send header"
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm=\"Test\"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        ''' Present frontpage with user authentication. '''
        if self.headers.getheader('Authorization') == None:
            self.do_AUTHHEAD()
            self.wfile.write('no auth header received')
            pass

        elif self.headers.getheader('Authorization') != None:
            authhead=self.headers.getheader('Authorization')[6:]
            username=base64.b64decode(authhead).split(':')[0]
            pwd=base64.b64decode(authhead).split(':')[1]
            ldapauth=ReferLdap()
            ldapauth.ldapauth(username,pwd)
            if ldapauth.authSF:
                self.do_HEAD()
                self.wfile.write(self.headers.getheader('Authorization'))
                self.wfile.write('authenticated!')
                pass
            else:
                self.do_AUTHHEAD()
                self.wfile.write(self.headers.getheader('Authorization'))
                self.wfile.write('not authenticated')
                pass

httpd = SocketServer.TCPServer(("", 10001), Handler)
httpd.serve_forever()

if __name__ == '__main__':
    main()
