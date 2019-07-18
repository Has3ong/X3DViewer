from . import *

# SFVec4f defines an abstract node interface.
# SFVec4f is a 4-tuple set of single-precision floating-point values, specifying a 3D homogeneous vector.
class CSFVec4f(CX3DField):

    m_values = [0.0, 0.0, 0.0, 0.0]

    def __init__(self):
        self.m_values = [0.0, 0.0, 0.0, 0.0]

    # Return array of 4-tuple float results array [] from type SFVec4f
    def getValue(self, value):
        value[0] = self.m_values[0]
        value[1] = self.m_values[1]
        value[2] = self.m_values[2]
        value[3] = self.m_values[3]

    # Assign 4-tuple float array [] to type SFVec4f
    def setValue1(self, value):
        self.m_values[0] = value[0]
        self.m_values[1] = value[1]
        self.m_values[2] = value[2]
        self.m_values[3] = value[3]

    def setValue4(self, x, y, z, w):
        self.m_values[0] = x
        self.m_values[1] = y
        self.m_values[2] = z
        self.m_values[3] = w

    def x(self):
        return self.m_values[0]

    def y(self):
        return self.m_values[1]

    def z(self):
        return self.m_values[2]

    def w(self):
        return self.m_values[3]