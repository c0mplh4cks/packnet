"""

 PACKNET  -  c0mplh4cks

 DATATYPE
    LEN



"""





# === Importing Dependencies === #
from struct import pack, unpack
from . import INT







# === LEN === #
class LEN:
    def __init__(self, header=0, payload=0, total=0):
        self.length = (header, payload, total)


    def __str__(self):
        return f"({ self.header }, { self.payload }, { self.total })"


    def __getitem__(self, key):
        if key == 0 or key == "header":
            return self.header
        elif key == 1 or key == "payload":
            return self.payload
        elif key == 2 or key == "total":
            return self.total
        else:
            raise IndexError


    def __setitem__(self, key, value):
        if key == 0 or key == "header":
            self.header = value
        elif key == 1 or key == "payload":
            self.payload = value
        elif key == 2 or key == "total":
            self.total = value
        else:
            raise IndexError



    @property
    def header(self):
        return self.__header


    @header.setter
    def header(self, value):
        self.__header = INT(value)


    @property
    def payload(self):
        return self.__payload


    @payload.setter
    def payload(self, value):
        self.__payload = INT(value)


    @property
    def total(self):
        if not int(self.__total):
            return INT( int(self.header) + int(self.payload) )
        return self.__total


    @total.setter
    def total(self, value):
        self.__total = INT(value)


    @property
    def length(self):
        return ( int(self.header), int(self.payload), int(self.total) )


    @length.setter
    def length(self, value):
        self.header, self.payload, self.total = value
