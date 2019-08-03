from . import *

# SFVec2f defines an abstract node interface.
# SFVec2f is a 2-tuple pair of SFFloat values. Hint: SFVec2f can be used to specify a 2D single-precision coordinate.
class CSFVec2f(CX3DField):

    m_values = [0.0, 0.0]

    def __init__(self):
        self.m_values = [0.0, 0.0]

    # Return array of 2-tuple float results array [] from type SFVec2f
    def getValue(self, value):
        value[0] = self.m_values[0]
        value[1] = self.m_values[1]

    # Assign 2-tuple float array [] to type SFVec2f
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