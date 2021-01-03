from . import *

# SFRotation defines an abstract node interface.
# SFRotation is an axis-angle 4-tuple, indicating X-Y-Z direction plus angle orientation about that axis. The first three values specify a normalized rotation axis vector about which the rotation takes place. (Thus the first three values shall be within the range [-1..+1] in order to represent a normalized unit vector. Problem: scientific notation allows leading digit.) The fourth value specifies the amount of right-handed rotation about that axis in radians.

class CSFRotation(CX3DField):

    def __init__(self):
        self.m_values = [0.0, 0.0, 0.0, 0.0]

    # Return array of 4-tuple float results array in radians from type SFRotation
    def getValue(self, value):
        value[0] = self.m_values[0]
        value[1] = self.m_values[1]
        value[2] = self.m_values[2]
        value[3] = self.m_values[3]

    # Assign 4-tuple float array in radians to type SFRotation
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