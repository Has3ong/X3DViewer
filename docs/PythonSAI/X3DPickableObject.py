from . import *

# X3DPickableObject defines an abstract node interface.
class CX3DPickableObject(CX3DNode):
    m_strNodeName = "X3DPickableObject"
    def __init__(self):
        self.m_strNodeName = "X3DPickableObject"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0
 
    # Return array of String results array ["ALL","NONE","TERRAIN",...] from MFString inputOutput field named "objectType"
    def getObjectType (self):
        pass

    # Return number of primitive values in "objectType" array
    def getNumObjectType (self):
        pass

    # Assign String array ["ALL","NONE","TERRAIN",...] to MFString inputOutput field named "objectType"
    def setObjectType1 (self, values, size):
        pass

    # Assign single String value ["ALL","NONE","TERRAIN",...] as the MFString array for inputOutput field named "objectType"
    def setObjectType2 (self, value):
        pass

    # Return bool result from SFBool inputOutput field named "pickable"
    def getPickable (self):
        pass

    # Assign bool value to SFBool inputOutput field named "pickable"
    def setPickable (self, value):
        pass