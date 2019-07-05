from . import *

# ClipPlane defines a concrete node interface that extends interface X3DChildNode.
class CClipPlane(CX3DChildNode):
    m_strNodeName = "ClipPlane"
    def __init__(self):
        self.m_strNodeName = "ClipPlane"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return boolean result from SFBool inputOutput field named "enabled"
    def getEnabled (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "enabled"
    def setEnabled (self, value):
        pass

    # Return array of 4-tuple float results array [] from SFVec4f inputOutput field named "plane"
    def getPlane (self):
        pass

    # Assign 4-tuple float array [] to SFVec4f inputOutput field named "plane"
    def setPlane (self, value):
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
