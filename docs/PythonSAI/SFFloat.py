from . import *

class CSFFloat(CX3DField):
    m_value = 0.0

    def __init__(self):
        m_value = 0.0
        
    def getValue(self):
        return self.m_value
    
    def setValue(self, value):
        self.m_value = value