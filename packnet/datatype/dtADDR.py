"""

 PACKNET  -  c0mplh4cks

 DATATYPE
    ADDR



"""





# === Importing Dependencies === #
from struct import pack, unpack
from . import IP, IPv6, MAC, INT







# === ADDR === #
class ADDR:
    def __init__(self, ip="", port=0, mac="", ipv6=""):
        self.addr = [ip, port, mac]
        self.ipv6 = ipv6


    def __str__(self):
        return f"['{ self.ip }', { self.port }, '{ self.mac }']"


    def __getitem__(self, key):
        if key == 0 or key == "ip":
            return self.ip
        elif key == 1 or key == "port":
            return self.port
        elif key == 2 or key == "mac":
            return self.mac
        else:
            raise IndexError


    def __setitem__(self, key, value):
        if key == 0 or key == "ip":
            self.ip = value
        elif key == 1 or key == "port":
            self.port = value
        elif key == 2 or key == "mac":
            self.mac = value
        else:
            raise IndexError



    @property
    def ip(self):
        return self.__ip


    @ip.setter
    def ip(self, value):
        self.__ip = IP(value)


    @property
    def ipv6(self):
        return self.__ipv6


    @ipv6.setter
    def ipv6(self, value):
        self.__ipv6 = IPv6(value)


    @property
    def port(self):
        return self.__port


    @port.setter
    def port(self, value):
        self.__port = INT(value, 2, "big")


    @property
    def mac(self):
        return self.__mac


    @mac.setter
    def mac(self, value):
        self.__mac = MAC(value)


    @property
    def addr(self):
        return [ str(self.ip), int(self.port), str(self.mac) ]


    @addr.setter
    def addr(self, value):
        self.ip, self.port, self.mac = value
