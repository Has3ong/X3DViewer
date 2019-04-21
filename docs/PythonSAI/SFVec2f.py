from . import *

class CSFVec2f(CX3DField):

    m_values = [0.0, 0.0]

    def __init__(self):
        self.m_values = [0.0, 0.0]

    def getValue(self, value):
        value[0] = self.m_values[0]
        value[1] = self.m_values[1]
    
    def setValue1(self, value):
        self.m_values[0] = value[0]
        self.m_values[1] = value[1]

    def setValue2(self, x, y):
        self.m_valeus[0] = x
        self.m_values[1] = y

    def x(self):
        return self.m_values[0]

    def y(self):
        return self.m_values[1]