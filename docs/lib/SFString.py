from X3DLib import *

class CSFString(CX3DField):
    m_value = ""

    def getValue(self):
        return self.m_value

    def setValue(self, value):
        self.m_value = value