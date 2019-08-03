from . import *

# SFVec4d defines an abstract node interface.
# SFVec4d is a 4-tuple set of double-precision floating-point values, specifying a 3D homogeneous vector.
class CSFVec4d(CX3DField):

    m_values = [0.0, 0.0, 0.0, 0.0]

    def __init__(self):
        self.m_values = np.double([0.0, 0.0, 0.0, 0.0])

    # Return array of 4-tuple double results array [] from type SFVec4d
    def getValue(self, value):
        value[0] = self.m_values[0]
        value[1] = self.m_values[1]
        value[2] = self.m_values[2]
        value[3] = self.m_values[3]

    # Assign 4-tuple double array [] to type SFVec4d
    def setValue1(self, value):
        self.m_values[0] = np.double(value[0])
        self.m_values[1] = np.double(value[1])
        self.m_values[2] = np.double(value[2])
        self.m_values[3] = np.double(value[3])

    def setValue4(self, x, y, z, w):
        self.m_values[0] = np.double(x)
        self.m_values[1] = np.double(y)
        self.m_values[2] = np.double(z)
        self.m_values[3] = np.double(w)

    def x(self):
        return self.m_values[0]

    def y(self):
        return self.m_values[1]

    def z(self):
        return self.m_values[2]

    def w(self):
        return self.m_values[3]