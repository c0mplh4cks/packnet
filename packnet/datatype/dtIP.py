"""

 PACKNET  -  c0mplh4cks

 DATATYPE
    IP



"""





# === Importing Dependencies === #
from struct import pack, unpack







# === IP === #
class IP:
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
    def decode(encoded):
        encoded = encoded[:4]
        ip = ".".join( [str(n) for n in encoded] )
        return len(encoded), ip


    @staticmethod
    def encode(ip):
        encoded = b"".join( [pack(">B", int(n)) for n in ip.split(".")] )
        return encoded


    def to_bytes(self):
        return self.encode( self.ip )


    def from_bytes(self, encoded):
        length, self.ip = self.decode(encoded)
        return length, self.ip
