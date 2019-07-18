from . import *

# SFString defines an abstract node interface.
# SFString defines a single string encoded with the UTF-8 universal character set.
class CSFString(CX3DField):
    m_value = ""

    # Return String result [] from type SFString
    def getValue(self):
        return self.m_value

    # Assign String value [] to type SFString
    def setValue(self, value):
        self.m_value = value