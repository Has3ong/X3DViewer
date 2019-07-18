from . import *

# X3DComposableVolumeRenderStyleNode defines an abstract node interface that extends interfaces X3DNode.
class CX3DComposableVolumeRenderStyle(CX3DVolumeRenderStyleNode):
    m_strNodeName = "X3DComposableVolumeRenderStyle"
    def __init__(self):
        self.m_strNodeName = "X3DComposableVolumeRenderStyle"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return bool result from SFBool inputOutput field named "enabled"
    def getEnabled1 (self):
        pass

    # Assign bool value to SFBool inputOutput field named "enabled"
    def setEnabled1 (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return bool result from SFBool inputOutput field named "enabled"
    def getEnabled2 (self):
        pass

    # Assign bool value to SFBool inputOutput field named "enabled"
    def setEnabled2 (self, value):
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