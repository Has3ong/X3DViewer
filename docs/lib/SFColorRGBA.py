from X3DLib import *

class CSFColorRGBA(CX3DField):
    m_values = [0.0, 0.0, 0.0, 0.0]

    def getValue(self, result):
        result[0] = self.m_values[0]
        result[1] = self.m_values[1]
        result[2] = self.m_values[2]
        result[3] = self.m_values[3]

    def setValue1(self, color):
        self.m_values[0] = color[0]
        self.m_values[1] = color[1]
        self.m_values[2] = color[2]
        self.m_values[3] = color[3]

    def setValue3(self, r, g, b):
        self.m_values[0] = r
        self.m_values[1] = g
        self.m_values[2] = b
        self.m_values[3] = a

    def r(self):
        return self.m_values[0]

    def g(self):
        return self.m_values[1]

    def b(self):
        return self.m_values[2]

    def a(self):
        return self.m_values[3]