from . import *

# X3DSequencerNode defines an abstract node interface that extends interfaces X3DNode.
class CX3DSequencerNode(CX3DChildNode):
    m_strNodeName = "X3DSequencerNode"
    def __init__(self):
        self.m_strNodeName = "X3DSequencerNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Assign bool value to SFBool inputOnly field named "next"
    def setNext (self, value):
        pass

    # Assign bool value to SFBool inputOnly field named "previous"
    def setPrevious (self, value):
        pass

    # Assign float value [] to SFFloat inputOnly field named "set_fraction"
    def setFraction (self, value) :
        pass

    # Return array of float results array [] from MFFloat inputOutput field named "key"
    def getKey (self):
        pass

    # Return number of primitive values in "key" array
    def getNumKey (self):
        pass

    # Assign float array [] to MFFloat inputOutput field named "key"
    def setKey1 (self, values, size) :
        pass

    # Assign single float value [] as the MFFloat array for inputOutput field named "key"
    def setKey2 (self, value) :
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return X3DMetadataObject result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "metadata"
    def getMetadata(self):
        pass

    # Assign X3DMetadataObject value (using a properly typed node) to SFNode inputOutput field named "metadata"
    def setMetadata1 (self, node):
        pass

    # Assign X3DMetadataObject value (using a properly typed protoInstance)
    def setMetadata2 (self, protoInstance):
        pass