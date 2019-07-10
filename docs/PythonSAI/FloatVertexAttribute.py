from . import *

# FloatVertexAttribute defines a concrete node interface that extends interface X3DVertexAttributeNode.
class CFloatVertexAttribute(CX3DVertexAttributeNode):
    m_strNodeName = "FloatVertexAttribute"
    def __init__(self):
        self.m_strNodeName = "FloatVertexAttribute"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of float results array [] from MFFloat inputOutput field named "value"
    def getValue (self):
        pass

    # Return number of primitive values in "value" array
    def getNumValue (self):
        pass

    # Assign float array [] to MFFloat inputOutput field named "value"
    def setValue1 (self, values, size):
        pass

    # Assign single float value [] as the MFFloat array for inputOutput field named "value"
    def setValu2e (self, value):
        pass

    # Return int result [] from  type initializeOnly field named "numComponents"
    def getNumComponents (self):
        pass

    # Assign int value [] to  type initializeOnly field named "numComponents"
    def setNumComponents (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return String result [] from SFString inputOutput field named "name"
    def getName (self):
        pass

    # Assign String value [] to SFString inputOutput field named "name"
    def setName (self, value):
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
