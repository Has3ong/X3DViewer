from . import *

# SFBool defines an abstract node interface.
# SFBool is a logical type with possible values (true|false) to match the XML bool type. Hint: X3D SFBool values are lower case (true|false) in order to maintain compatibility with other XML documents.

class CSFBool(CX3DField):
    m_value = False

    def __init__(self, value = None):        
        if value == None:
            self.m_value = False

        self.m_value = False

    # Return bool result [] from type SFBool
    def getValue(self):
        return self.m_value

    # Assign bool value [] to type SFBool
    def setValue(self, value):
        self.m_value = value