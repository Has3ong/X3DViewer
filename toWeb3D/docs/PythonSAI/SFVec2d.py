from . import *

# SFVec2d defines an abstract node interface.
# SFVec2d is a 2-tuple pair of SFDouble values. Array values are optionally separated by commas. Hint: SFVec2d can be used to specify a 2D double-precision coordinate.

class CSFVec2d(CX3DField):

    m_values = [0.0, 0.0]

    def __init__(self):
        self.m_values = np.double([0.0, 0.0])

    # Return array of 2-tuple double results array [] from type SFVec2d
    def getValue(self, value):
        value[0] = self.m_values[0]
        value[1] = self.m_values[1]

    # Assign 2-tuple double array [] to type SFVec2d
    def setValue1(self, value):
        self.m_values[0] = np.double(value[0])
        self.m_values[1] = np.double(value[1])

    def setValue2(self, x, y):
        self.m_valeus[0] = np.double(x)
        self.m_values[1] = np.double(y)

    def x(self):
        return self.m_values[0]

    def y(self):
        return self.m_values[1]