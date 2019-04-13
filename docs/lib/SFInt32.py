from X3DLib import *

class CSFInt32(CX3DField):
    m_value = 0

    def __init__(self):
        self.m_value = np.int32(0)

    def getValue(self):
        return self.m_value
    
    def setValue(self, value):
        self.m_value = np.int32(value)