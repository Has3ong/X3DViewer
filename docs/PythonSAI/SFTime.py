from . import *

# SFTime defines an abstract node interface.
# The SFTime field specifies a single time value. Time values are specified as a double-precision floating point number. Typically, SFTime fields represent the number of seconds since Jan 1, 1970, 00:00:00 GMT.

class CSFTime(CX3DField):
    m_value = 0.0

    def __init__(self, value = None):        
        if value == None:
            self.m_value = False

        self.m_value = False

    # Return double result in seconds from type SFTime
    def getValue(self):
        return self.m_value

    # Return long value in nanoseconds from type SFTime
    def getJavaValue (self):
        pass

    # Assign double value in seconds to type SFTime
    def setValue1(self, value):
        self.m_value = value

    # Assign long value in nanoseconds using System.nanoTime() to type SFTime
    def setValue2 (self, value):
        pass

    def getSource(self):
        return self.m_tofield[0]