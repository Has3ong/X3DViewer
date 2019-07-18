from . import *

# MFString defines an abstract node interface.
# MFString is an array of SFString values, each "quoted" and separated by whitespace. Array values are optionally separated by commas.
class CMFString(CMField):

    m_Values = []

    # Return array of String results array [] from type MFString
    def getValue1(self):
        return self.m_Values

    # Utility method to return single value from MFString array
    def getValue2(self, index):
        return self.m_Values[index]

    # Assign String array [] to type MFString
    def setValue1(self, size, values):
        for i in range (0, size):
            self.m_Values.append(values[i])

    # Utility method to set a single value in MFString array
    def setValue2(self, index, value):
        self.m_Values.insert(index, value)

    # Utility method to append a single value to MFString array
    def append(self, value):
        self.m_Values.append(value)

    # Utility method to insert a single value in MFString array
    def insertValue(self, index, value):
        self.m_Values.insert(index, value)

    def size(self):
        return len(self.m_Values)
    
    def clear(self):
        self.m_Values.clear()

    def remove(self, index):
        del self.m_Values[index]