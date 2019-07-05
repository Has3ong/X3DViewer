from . import *

# BooleanFilter defines a concrete node interface that extends interface X3DChildNode.
class CBooleanFilter(CX3DChildNode):
    m_strNodeName = "BooleanFilter"
    def __init__(self):
        self.m_strNodeName = "BooleanFilter"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

    # Assign boolean value to SFBool inputOnly field named "set_boolean"
    def setBoolean (self, value):
        pass

    # Return boolean result from SFBool outputOnly field named "inputFalse"
    def getInputFalse (self):
        pass

    # Return boolean result from SFBool outputOnly field named "inputNegate"
    def getInputNegate (self):
        pass

    # Return boolean result from SFBool outputOnly field named "inputTrue"
    def getInputTrue (self):
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
