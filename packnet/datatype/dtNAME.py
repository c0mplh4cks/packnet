"""

 PACKNET  -  c0mplh4cks

 DATATYPE
    NAME



"""





# === Importing Dependencies === #
from struct import pack, unpack







# === NAME === #
class NAME:
    def __init__(self, name=""):
        self.name = name


    def __str__(self):
        return f"{ self.name }"


    def __len__(self):
        return len( self.to_bytes() )



    @property
    def size(self):
        return len( self.to_bytes() )


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, value):
        self.__name = value if type(value) != bytes else self.decode(value)[1]



    @staticmethod
    def decode(encoded):
        labels = []
        name = encoded

        while True:
            l = name[0]
            if l == 0: break
            labels.append( name[1:1+l].decode() )
            name = name[1+l:]

        return len(encoded), ".".join(labels)


    @staticmethod
    def encode(name):
        encoded = b"".join([ b for label in name.split(".") for b in [ pack(">B", len(label)), label.encode() ] ]) + b"\x00"
        return encoded


    @classmethod
    def decompress(cls, encoded, header):
        i = 0
        for _ in range( len(encoded) ):
            l = encoded[i]

            if l == 0:
                return cls.decode(encoded)
            elif (l >> 6) == 3:
                pointer = unpack( ">H", encoded[i:i+2] )[0] - 0xc000
                return i+2, cls.decode( encoded[:i] + header[pointer:] )[1]

            i += 1+l


    @classmethod
    def compress(cls, name, header):
        encoded = cls.encode( name )
        i = 0

        while True:
            f = header.find( encoded[i:] )
            if f != -1: break
            l = encoded[i]
            i += 1+l

        return encoded[:i] + pack( ">H", 0xc000+f )


    def to_bytes(self, header=b""):
        return self.compress( self.name, header )


    def from_bytes(self, encoded, header=b""):
        length, self.name = self.decompress( encoded, header )
        return length, self.name
