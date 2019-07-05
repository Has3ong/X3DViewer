from . import *

# BooleanToggle defines a concrete node interface that extends interface X3DChildNode.
class CBooleanToggle(CX3DChildNode):
    m_strNodeName = "BooleanToggle"
    def __init__(self):
        self.m_strNodeName = "BooleanToggle"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Assign boolean value to SFBool inputOnly field named "set_boolean"
    def setBoolean (self, value):
        pass

    # Return boolean result from SFBool inputOutput field named "toggle"
    def getToggle (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "toggle"
    def setToggle (self, value):
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