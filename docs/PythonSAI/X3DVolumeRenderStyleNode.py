from . import *

# X3DVolumeRenderStyleNode defines an abstract node interface that extends interface .
class CX3DVolumeRenderStyleNode(CX3DNode):
    m_strNodeName = "X3DVolumeRenderStyleNode"
    def __init__(self):
        self.m_strNodeName = "X3DVolumeRenderStyleNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return bool result from SFBool inputOutput field named "enabled"
    def getEnabled (self):
        pass

    # Assign bool value to SFBool inputOutput field named "enabled"
    def setEnabled (self, value):
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