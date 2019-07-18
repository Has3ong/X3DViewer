from . import *

# SFInt32 defines an abstract node interface.
# An SFInt32 field specifies one 32-bit signed integer.
class CSFInt32(CX3DField):
    m_value = 0

    def __init__(self):
        self.m_value = np.int32(0)

    # Return int result [] from type SFInt32
    def getValue(self):
        return self.m_value

    # Assign int value [] to type SFInt32
    def setValue(self, value):
        self.m_value = np.int32(value)