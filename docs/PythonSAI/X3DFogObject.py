from . import *

# X3DFogObject defines an abstract node interface.
class CX3DFogObject(CX3DNode):
    m_strNodeName = "X3DFogObject"
    def __init__(self):
        self.m_strNodeName = "X3DFogObject"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of 3-tuple float results array using RGB values [0..1] from SFColor inputOutput field named "color"
    def getColor (self):
        pass

    # Assign 3-tuple float array using RGB values [0..1] to SFColor inputOutput field named "color"
    def setColor (self, color) :
        pass

    # Return String enumeration result ("LINEAR"|"EXPONENTIAL") from fogTypeValues type inputOutput field named "fogType"
    def getFogType (self):
        pass

    # Assign String enumeration value ("LINEAR"|"EXPONENTIAL") to fogTypeValues type inputOutput field named "fogType"
    def setFogType (self, value) :
        pass

    # Return float result [] from  type inputOutput field named "visibilityRange"
    def getVisibilityRange (self):
        pass

    # Assign float value [] to  type inputOutput field named "visibilityRange"
    def setVisibilityRange (self, value) :
        pass