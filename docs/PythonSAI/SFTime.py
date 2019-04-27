from . import *

class CSFTime(CX3DField):
    m_value = 0.0

    def __init__(self, value = None):        
        if value == None:
            self.m_value = False

        self.m_value = False

    def getValue(self):
        return self.m_value

    def setValue(self, value):
        self.m_value = value

    def getSource(self):
        return self.m_tofield[0]