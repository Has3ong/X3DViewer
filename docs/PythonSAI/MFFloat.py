from . import *

# MFFloat defines an abstract node interface.
# MFFloat is an array of SFFloat values, i.e. a single-precision floating-point array type. Array values are optionally separated by commas.
class CMFFloat(CMField):

    m_Values = []

    def __init__(self):
        self.m_Values = []

    # Return array of float results array [] from type MFFloat
    def getValue1(self):
        return self.m_Values

    # Utility method to return single value from MFFloat array
    def getValue2(self, index):
        return self.m_Values[index]

    # Assign float array [] to type MFFloat
    def setValue1(self, size, values):
        for i in range (0, size):
            self.m_Values.append(values[i])

    # Utility method to set a single value in MFFloat array
    def setValue2(self, index, value):
        self.m_Values.insert(index, value)

    # Utility method to append a single value to MFFloat array
    def append(self, value):
        self.m_Values.append(value)

    # Utility method to insert a single value in MFFloat array
    def insertValue(self, index, value):
        self.m_Values.insert(index, value)

    def size(self):
        return len(self.m_Values)
    
    def clear(self):
        self.m_Values.clear()

    def remove(self, index):
        del self.m_Values[index]