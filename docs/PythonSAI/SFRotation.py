from . import *

class CSFRotation(CX3DField):
    m_values = [0.0, 0.0, 0.0, 0.0]

    def getValue(self, value):
        value[0] = self.m_values[0]
        value[1] = self.m_values[1]
        value[2] = self.m_values[2]
        value[3] = self.m_values[3]

    def setValue1(self, value):
        self.m_values[0] = value[0]
        self.m_values[1] = value[1]
        self.m_values[2] = value[2]
        self.m_values[3] = value[3]

    def setValue4(self, x, y, z, rot):
        self.m_values[0] = x
        self.m_values[1] = y
        self.m_values[2] = z
        self.m_values[3] = rot

    def x(self):
        return self.m_values[0]

    def y(self):
        return self.m_values[1]

    def z(self):
        return self.m_values[2]

    def rot(self):
        return self.m_values[3]