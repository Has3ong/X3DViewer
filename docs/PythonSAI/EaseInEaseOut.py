from . import *

# EaseInEaseOut defines a concrete node interface that extends interface X3DChildNode.
class CEaseInEaseOut(CX3DNode):
    m_strNodeName = "EaseInEaseOut"
    def __init__(self):
        self.m_strNodeName = "EaseInEaseOut"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Assign float value [] to SFFloat inputOnly field named "set_fraction"
    def setFraction (self, value):
        pass

    # Return float result [] from SFFloat outputOnly field named "modifiedFraction_changed"
    def getModifiedFraction (self):
        pass

    # Return array of 2-tuple float results array [] from MFVec2f inputOutput field named "easeInEaseOut"
    def getEaseInEaseOut (self):
        pass

    # Return number of 2-tuple primitive values in "easeInEaseOut" array
    def getNumEaseInEaseOut (self):
        pass

    # Assign 2-tuple float array [] to MFVec2f inputOutput field named "easeInEaseOut"
    def setEaseInEaseOut (self, values, size):
        pass

    # Return array of float results array [] from MFFloat inputOutput field named "key"
    def getKey (self):
        pass

    # Return number of primitive values in "key" array
    def getNumKey (self):
        pass

    # Assign float array [] to MFFloat inputOutput field named "key"
    def setKey1 (self, values, size):
        pass

    # Assign single float value [] as the MFFloat array for inputOutput field named "key"
    def setKey2 (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return X3DMetadataObject result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "metadata"
    def getMetadata (self):
        pass

    # Assign X3DMetadataObject value (using a properly typed node) to SFNode inputOutput field named "metadata"
    def setMetadata1 (self, node):
        pass

    # Assign X3DMetadataObject value (using a properly typed protoInstance)
    def setMetadata2 (self, protoInstance):
        pass
