from . import *

# MFInt32 defines an abstract node interface.
# An MFInt32 field defines an array of 32-bit signed integers. Array values are optionally separated by commas.
class CMFInt32(CMField):

    m_Values = []

    def __init__(self):
        self.m_Values = []

    # Return MFInt32 result [] from type MFInt32
    def getValue1(self):
        return self.m_Values

    # Utility method to return single value from MFInt32 array
    def getValue2(self, index):
        return self.m_Values[index]

    # Assign MFInt32 value [] to type MFInt32
    def setValue1(self, size, values):
        for i in range (0, size):
            self.m_Values.append(np.int32(values[i]))

    # Utility method to set a single value in MFInt32 array
    def setValue2(self, index, value):
        self.m_Values.insert(index, np.int32(value))

    # Utility method to append a single value to MFInt32 array
    def append(self, value):
        self.m_Values.append(np.int32(value))

    # Utility method to insert a single value in MFInt32 array
    def insertValue(self, index, value):
        self.m_Values.insert(index, np.int32(value))

    def size(self):
        return len(self.m_Values)
    
    def clear(self):
        self.m_Values.clear()

    def remove(self, index):
        del self.m_Values[index]