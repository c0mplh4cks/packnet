"""

 PACKNET  -  c0mplh4cks

 DATATYPE
    IPv6



"""





# === Importing Dependencies === #
from struct import pack, unpack







# === IPv6 === #
class IPv6:
    def __init__(self, ip=""):
        self.ip = ip


    def __str__(self):
        return f"{ self.ip }"


    def __len__(self):
        return len( self.to_bytes() )



    @property
    def ip(self):
        return self.__ip


    @ip.setter
    def ip(self, value):
        self.__ip = value if type(value) != bytes else self.decode(value)[1]



    @staticmethod
    def encode(ip):
        ip = ip.split(":")

        if "" in ip:
            n = ip.index("")
            for i in range( 9-len(ip) ):
                ip.insert(n, "0")
            ip.remove("")

        return b"".join([ pack(">H", int(i, 16)) for i in ip ])


    @staticmethod
    def decode(encoded):
        ip = encoded[:16]
        parts = [ ip[i:i+2] for i in range(0, len(ip), 2) ]
        parts = [ hex(unpack(">H", p)[0])[2:] for p in parts ]
        ip = ":".join(parts)
        for i in range(6, 0, -1):
            z = ":0" * i
            if z in ip:
                ip = ip.replace(z, ":", 1)
        return len(encoded), ip


    def to_bytes(self):
        return self.encode( self.ip )


    def from_bytes(self, encoded):
        length, self.ip = self.decode(encoded)
        return length, self.ip
