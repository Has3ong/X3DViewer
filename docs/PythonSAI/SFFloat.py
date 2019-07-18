from . import *

# SFFloat defines an abstract node interface.
# SFFloat is a single-precision floating-point type.
class CSFFloat(CX3DField):
    m_value = 0.0

    def __init__(self):
        m_value = 0.0

    # Return float result [] from type SFFloat
    def getValue(self):
        return self.m_value

    # Assign float value [] to type SFFloat
    def setValue(self, value):
        self.m_value = value