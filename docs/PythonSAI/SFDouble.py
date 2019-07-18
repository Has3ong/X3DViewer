from . import *

# SFDouble defines an abstract node interface.
# SFDouble is a double-precision floating-point type. Array values are optionally separated by commas. See GeoVRML 1.0 Recommended Practice, Section 2.3, Limitations of Single Precision for rationale.
class CSFDouble(CX3DField):
    m_value = 0.0

    def __init__(self):
        m_value = np.double(0.0)

    # Return double result [] from type SFDouble
    def getValue(self):
        return self.m_value

    # Assign double value [] to type SFDouble
    def setValue(self, value):
        self.m_value = np.double(value)