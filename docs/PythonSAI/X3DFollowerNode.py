from . import *

# X3DFollowerNode defines an abstract node interface that extends interfaces X3DNode.
class CX3DFollowerNode(CX3DChildNode):
    m_strNodeName = "X3DFollowerNode"
    def __init__(self):
        self.m_strNodeName = "X3DFollowerNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return bool result from SFBool outputOnly field named "isActive"
    def getIsActive (self):
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