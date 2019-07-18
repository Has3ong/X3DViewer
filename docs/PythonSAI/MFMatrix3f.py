from . import *

# MFMatrix3f defines an abstract node interface.
# MFMatrix3f specifies zero or more 3x3 matrices of single-precision floating point numbers, organized in row-major fashion.
class CMFMatrix3f (CMField) :

    # Return array of float results array [] from type MFMatrix3f
    def getValue1 (self):
        pass

    # Return array of float results array [] from type MFMatrix3f
    def getValue2 (self, result):
        pass

    # Utility method to return single value from MFMatrix3f array
    def getValue3 (self, index):
        pass

    # Assign float array [] to type MFMatrix3f
    def setValue1 (self, size, values) :
        pass

    # Assign float array [] to type MFMatrix3f
    def setValue2 (self, values) :
        pass

    # Utility method to set a single value in MFMatrix3f array
    def setValue3 (self, index, value):
        pass

    # Utility method to append a single value to MFMatrix3f array
    def append (self, value):
        pass

    # Utility method to insert a single value in MFMatrix3f array
    def insertValue (self, index, value):
        pass