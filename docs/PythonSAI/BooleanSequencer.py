from . import *

# BooleanSequencer defines a concrete node interface that extends interface X3DSequencerNode.
class CBooleanSequencer(CX3DSequencerNode):
    m_strNodeName = "BooleanSequencer"
    def __init__(self):
        self.m_strNodeName = "BooleanSequencer"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return boolean result from SFBool outputOnly field named "value_changed"
    def getValue (self):
        pass

    # Return array of boolean results array from MFBool inputOutput field named "keyValue"
    def getKeyValue (self):
        pass

    # Return number of primitive values in "keyValue" array
    def getNumKeyValue (self):
        pass

    # Assign boolean array to MFBool inputOutput field named "keyValue"
    def setKeyValue1 (self, values, size):
        pass

    # Assign single boolean value as the MFBool array for inputOutput field named "keyValue"
    def setKeyValue2 (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Assign boolean value to SFBool inputOnly field named "next"
    def setNext (self, value):
        pass

    # Assign boolean value to SFBool inputOnly field named "previous"
    def setPrevious (self, value):
        pass

    # Assign float value [] to SFFloat inputOnly field named "set_fraction"
    def setFraction (self, value):
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

    # Return X3DMetadataObject result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "metadata"
    def getMetadata (self):
        pass

    # Assign X3DMetadataObject value (using a properly typed node) to SFNode inputOutput field named "metadata"
    def setMetadata1 (self, node):
        pass

    # Assign X3DMetadataObject value (using a properly typed protoInstance)
    def setMetadata2 (self, protoInstance):
        pass