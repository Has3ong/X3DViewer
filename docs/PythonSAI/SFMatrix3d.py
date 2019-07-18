from . import *

# SFMatrix3d defines an abstract node interface.
# SFMatrix3d specifies a 3x3 matrix of double-precision floating point numbers, organized in row-major fashion.
class CSFMatrix3f(CX3DField):
    pass

    # Return array of double results array [] from type SFMatrix3d
    def getValue(self):
        pass

    # Assign double array [] to type SFMatrix3d
    def setValue(self, value):
        pass