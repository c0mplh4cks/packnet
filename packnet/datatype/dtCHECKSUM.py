"""

 PACKNET  -  c0mplh4cks

 DATATYPE
    CHECKSUM



"""





# === Importing Dependencies === #
from struct import pack, unpack
from . import INT







# === CHECKSUM === #
class CHECKSUM:
    def __init__(self, *args):
        self.checksum = args


    def __str__(self):
        return f"{ self.value }"


    def __int__(self):
        return f"{ self.value.__int__ }"



    @property
    def checksum(self):
        return self.__value


    @checksum.setter
    def checksum(self, data):
        if type(data) == bytes:
            value = data
        else:
            data = b"".join([ v.to_bytes() if type(v) != bytes else v for v in data ])
            value = self.calculate(data)
        self.__value = INT( value, size=2 )



    @staticmethod
    def calculate(data):
        if (len(data) %2) != 0:
            data += b"\x00"

        values = unpack( f">{ len(data)//2 }H", data )
        n = sum(values) %65535
        n = 65535-n

        return n


    def to_bytes(self):
        return self.checksum.to_bytes()


    def from_bytes(self, encoded):
        encoded = encoded[:self.checksum.size]
        self.checksum = encoded
        return len(encoded), self.checksum
