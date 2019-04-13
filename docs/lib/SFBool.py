from X3DLib import *

class CSFBool(CX3DField):
    m_value = False

    def __init__(self, value = None):        
        if value == None:
            self.m_value = False

        self.m_value = False

    def getValue(self):
        return self.m_value

    def setValue(self, value):
        self.m_value = value