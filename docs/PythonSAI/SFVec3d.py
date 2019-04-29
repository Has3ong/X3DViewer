from . import *

class CSFVec3f(CX3DField):

    m_values = [0.0, 0.0, 0.0]

    def __init__(self):
        self.m_values = np.double([0.0, 0.0, 0.0])

    def getValue(self, value):
        value[0] = self.m_values[0]
        value[1] = self.m_values[1]
        value[2] = self.m_values[2]

    def setValue1(self, value):
        self.m_values[0] = np.double(value[0])
        self.m_values[1] = np.double(value[1])
        self.m_values[2] = np.double(value[2])

    def setValue3(self, x, y, z):
        self.m_values[0] = np.double(x)
        self.m_values[1] = np.double(y)
        self.m_values[2] = np.double(z)

    def x(self):
        return self.m_values[0]

    def y(self):
        return self.m_values[1]

    def z(self):
        return self.m_values[2]