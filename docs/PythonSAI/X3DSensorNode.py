from . import *

# X3DSensorNode defines an abstract node interface that extends interfaces X3DNode.
class CX3DSensorNode(CX3DNode):
    m_strNodeName = "CX3DSensorNode"
    DEF = ""

    enabled = True
    isActive = True
    def __init__(self):
        self.m_strNodeName = "CX3DSensorNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

        self.enable = True
        self.isActive = True

    # Return bool result from SFBool outputOnly field named "isActive"
    def getIsActive(self):
        return self.isActive

    def setIsActive(self, value):
        self.isActive = value

    # Return bool result from SFBool inputOutput field named "enabled"
    def getEnabled(self):
        return self.enabled

    # Assign bool value to SFBool inputOutput field named "enabled"
    def setEnabled(self, value):
        self.enabled = value

    def setDEF(self, value):
        self.DEF = value

    def getDEF(self):
        return self.DEF

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

    