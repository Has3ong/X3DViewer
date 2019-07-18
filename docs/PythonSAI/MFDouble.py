from . import *

# MFDouble defines an abstract node interface.
# MFDouble is an array of Double values, i.e. a double-precision floating-point array type. See GeoVRML 1.0 Recommended Practice, Section 2.3, Limitations of Single Precision for rationale. SFDouble/MFDouble are analagous to SFDouble/MFDouble. Array values are optionally separated by commas.
class CMFDouble(CMField):

    m_Values = []

    def __init__(self):
        self.m_Values = []

    # Return array of double results array [] from type MFDouble
    def getValue1(self):
        return self.m_Values

    # Utility method to return single value from MFDouble array
    def getValue2(self, index):
        return self.m_Values[index]

    # Assign double array [] to type MFDouble
    def setValue1(self, size, values):
        for i in range (0, size):
            self.m_Values.append(np.double(values[i]))

    # Utility method to set a single value in MFDouble array
    def setValue2(self, index, value):
        self.m_Values.insert(index, np.double(value))

    # Utility method to append a single value to MFDouble array
    def append(self, value):
        self.m_Values.append(np.double(value))

    # Utility method to insert a single value in MFDouble array
    def insertValue(self, index, value):
        self.m_Values.insert(index, np.double(value))

    def size(self):
        return len(self.m_Values)
    
    def clear(self):
        self.m_Values.clear()

    def remove(self, index):
        del self.m_Values[index]