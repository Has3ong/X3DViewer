from . import *

# BoundaryEnhancementVolumeStyle defines a concrete node interface that extends interface X3DComposableVolumeRenderStyleNode.
class CBoundaryEnhancementVolumeStyle(CX3DComposableVolumeRenderStyle):
    m_strNodeName = "BoundaryEnhancementVolumeStyle"
    def __init__(self):
        self.m_strNodeName = "BoundaryEnhancementVolumeStyle"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return float result [] from  type inputOutput field named "boundaryOpacity"
    def getBoundaryOpacity (self):
        pass

    # Assign float value [] to  type inputOutput field named "boundaryOpacity"
    def setBoundaryOpacity (self, value):
        pass

    # Return float result [] from  type inputOutput field named "opacityFactor"
    def getOpacityFactor (self):
        pass

    # Assign float value [] to  type inputOutput field named "opacityFactor"
    def setOpacityFactor (self, value):
        pass

    # Return float result [] from  type inputOutput field named "retainedOpacity"
    def getRetainedOpacity (self):
        pass

    # Assign float value [] to  type inputOutput field named "retainedOpacity"
    def setRetainedOpacity (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return boolean result from SFBool inputOutput field named "enabled"
    def getEnabled (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "enabled"
    def setEnabled (self, value):
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