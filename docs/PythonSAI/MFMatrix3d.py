from . import *

# MFMatrix3d defines an abstract node interface.
# MFMatrix3d specifies zero or more 3x3 matrices of double-precision floating point numbers, organized in row-major fashion.

class CMFMatrix3d (CMField) :

    # Return array of double results array [] from type MFMatrix3d
    def getValue1 (self):
        pass

    # Return array of double results array [] from type MFMatrix3d
    def getValue2 (self, result):
        pass

    # Utility method to return single value from MFMatrix3d array
    def getValue3 (self, index):
        pass

    # Assign double array [] to type MFMatrix3d
    def setValue1 (self, size, values) :
        pass

    # Assign double array [] to type MFMatrix3d
    def setValue2 (self, values) :
        pass

    # Utility method to set a single value in MFMatrix3d array
    def setValue3 (self, index, value):
        pass

    # Utility method to append a single value to MFMatrix3d array
    def append (self, value):
        pass

    # Utility method to insert a single value in MFMatrix3d array
    def insertValue (self, index, value):
        pass