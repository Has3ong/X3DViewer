from . import *

# SFMatrix3f defines an abstract node interface.
# SFMatrix3f specifies a 3x3 matrix of single-precision floating point numbers, organized in row-major fashion.
class CSFMatrix3f (CX3DField) :
    pass

    # Return array of float results array [] from type SFMatrix3f
    def getValue (self):
        pass

    # Assign float array [] to type SFMatrix3f
    def setValue (self, value) :
        pass