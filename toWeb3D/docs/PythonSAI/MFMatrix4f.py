from . import *

# MFMatrix4f defines an abstract node interface.
# MFMatrix4f specifies zero or more 4x4 matrices of single-precision floating point numbers, organized in row-major fashion.
class CMFMatrix4f(CMField):

    # Return array of float results array [] from type MFMatrix4f
    def getValue1 (self):
        pass

    # Return array of float results array [] from type MFMatrix4f
    def getValue2 (self, result):
        pass

    # Utility method to return single value from MFMatrix4f array
    def getValue3 (self, index):
        pass

    # Assign float array [] to type MFMatrix4f
    def setValue1 (self, size, values) :
        pass

    # Assign float array [] to type MFMatrix4f
    def setValue2 (self, values) :
        pass

    # Utility method to set a single value in MFMatrix4f array
    def setValue3 (self, index, value):
        pass

    # Utility method to append a single value to MFMatrix4f array
    def append (self, value):
        pass

    # Utility method to insert a single value in MFMatrix4f array
    def insertValue (self, index, value):
        pass