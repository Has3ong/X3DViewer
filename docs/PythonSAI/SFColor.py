from . import *

#  SFColor defines an abstract node interface.
class CSFColor(CX3DField):
    m_values = [0.0, 0.0, 0.0]

    def __init__(self):
        self.m_values = [0.0, 0.0, 0.0]

    # Return array of 3-tuple float results array using RGB values [0..1] from type SFColor
    def getValue(self, result):
        result[0] = self.m_values[0]
        result[1] = self.m_values[1]
        result[2] = self.m_values[2]

        return result

    # Assign 3-tuple float array using RGB values [0..1] to type SFColor
    def setValue1(self, color):
        self.m_values[0] = color[0]
        self.m_values[1] = color[1]
        self.m_values[2] = color[2]

    def setValue3(self, r, g, b):
        self.m_values[0] = r
        self.m_values[1] = g
        self.m_values[2] = b

    def r(self):
        return self.m_values[0]

    def g(self):
        return self.m_values[1]

    def b(self):
        return self.m_values[2]