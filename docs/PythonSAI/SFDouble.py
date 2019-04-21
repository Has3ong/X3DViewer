from . import *

class CSFDouble(CX3DField):
    m_value = 0.0

    def __init__(self):
        m_value = np.double(0.0)

    def getValue(self):
        return self.m_value
    
    def setValue(self, value):
        self.m_value = np.double(value)