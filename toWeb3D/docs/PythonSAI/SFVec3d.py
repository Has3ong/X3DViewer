from . import *

# SFVec3d defines an abstract node interface.
# SFVec3d is a 3-tuple triplet of SFDouble values. See GeoVRML 1.0 Recommended Practice, Section 2.3, Limitations of Single Precision. Hint: SFVec3d can be used to specify a georeferenced 3D coordinate.
class CSFVec3f(CX3DField):

    m_values = [0.0, 0.0, 0.0]

    def __init__(self):
        self.m_values = np.double([0.0, 0.0, 0.0])

    # Return array of 3-tuple double results array [] from type SFVec3d
    def getValue(self, value):
        value[0] = self.m_values[0]
        value[1] = self.m_values[1]
        value[2] = self.m_values[2]

    # Assign 3-tuple double array [] to type SFVec3d
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