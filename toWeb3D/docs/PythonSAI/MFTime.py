from . import *

# MFTime defines an abstract node interface.
# MFTime is an array of SFTime values. Array values are optionally separated by commas.
class CMFTime(CMField):

    m_Values = []

    # Return array of double results array in seconds from type MFTime
    def getValue1(self):
        return self.m_Values

    # Utility method to return single value from MFTime array
    def getValue2(self, index):
        return self.m_Values[index]

    # Utility method to return single long value in nanoseconds from MFTime array
    def getJavaValue(self, index):
        pass

    # Assign double array in seconds to type MFTime
    def setValue1(self, size, timestamps):
        pass

    # Assign long array in nanoseconds to type MFTime
    def setValue2(self, size, values):
        for i in range (0, size):
            self.m_Values.append(values[i])

    # Utility method to set a single value in MFTime array
    def setValue3(self, index, timestamp):
        pass

    # Utility method to set a single long value in nanoseconds using System.nanoTime() in MFTime array
    def setValue4(self, index, value):
        self.m_Values.insert(index, value)

    # Utility method to append a single value to MFTime array
    def append(self, value):
        self.m_Values.append(value)

    # Utility method to insert a single value in MFTime array
    def insertValue(self, index, value):
        self.m_Values.insert(index, value)

    def size(self):
        return len(self.m_Values)
    
    def clear(self):
        self.m_Values.clear()

    def remove(self, index):
        del self.m_Values[index]
