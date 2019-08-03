from . import *

# MFBool defines an abstract node interface.
# MFBool is an array of Bool values. Type MFBool was previously undefined in the VRML 97 Specification, but nevertheless needed for event utilities and scripting. Example use: MFBool is useful for defining a series of behavior states using a BooleanSequencer prototype.
class CMFBool(CMField):
    m_values = []

    # Return array of bool results array [] from type MFBool
    def getValue1(self):
        return self.m_values

    # Utility method to return single value from MFBool array
    def getValue2(self, index):
        bBool = self.m_values[index]
        return bBool

    # Assign bool array [] to type MFBoo
    def setValue1(self, size, values):
        for i in range (0, size):
            self.m_values.append(values)

    # Utility method to set a single value in MFBool array
    def setValue2(self, index, value):
        self.m_values.insert(index, value)

    # Utility method to append a single value to MFBool array
    def append(self, value):
        self.m_values.append(value)

    # Utility method to insert a single value in MFBool array
    def insertValue(self, index, value):
        self.m_values.insert(index, value)

    def size(self):
        return len(self.m_values)

    def clear(self):
        self.m_values.clear()

    def remove(self, index):
        del self.m_values[index]