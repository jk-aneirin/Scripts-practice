import socket
import fcntl
import struct

class GetIfStatus(object):
    def __init__(self,ifname='eth0'):
        self.ifname=ifname

    def get_ip_address(self):
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,
            struct.pack('256s',self.ifname[:15])
            )[20:24])

    def get_mac_address(self):
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        info=fcntl.ioctl(s.fileno(),0x8927,struct.pack('256s',self.ifname[:15]))
        return ''.join(['%02x:'%ord(char) for char in info[18:24]])[:-1]

    def get_network_bytes(self):
        for line in open('/proc/net/dev','r'):
            if self.ifname in line:
                data=line.split('%s:' % self.ifname)[1].split()
                rx_bytes,tx_bytes=(data[0],data[8])
                return (int(rx_bytes),int(tx_bytes))

m=GetIfStatus()
print m.get_network_bytes()
