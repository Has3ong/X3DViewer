from . import *

# MFMatrix4d defines an abstract node interface.
# MFMatrix4d specifies zero or more 4x4 matrices of double-precision floating point numbers, organized in row-major fashion.
class CMFMatrix4d (CMField) :

    # Return array of double results array [] from type MFMatrix4d
    def getValue1 (self):
        pass

    # Return array of double results array [] from type MFMatrix4d
    def getValue2 (self, result):
        pass

    # Utility method to return single value from MFMatrix4d array
    def getValue3 (self, index):
        pass

    # Assign double array [] to type MFMatrix4d
    def setValue1 (self, size, values) :
        pass

    # Assign double array [] to type MFMatrix4d
    def setValue2 (self, values) :
        pass

    # Utility method to set a single value in MFMatrix4d array
    def setValue3 (self, index, value):
        pass

    # Utility method to append a single value to MFMatrix4d array
    def append (self, value):
        pass

    # Utility method to insert a single value in MFMatrix4d array
    def insertValue (self, index, value):
        pass