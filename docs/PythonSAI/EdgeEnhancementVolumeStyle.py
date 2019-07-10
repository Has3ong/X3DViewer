from . import *

# EdgeEnhancementVolumeStyle defines a concrete node interface that extends interface X3DComposableVolumeRenderStyleNode.
class CEdgeEnhancementVolumeStyle(CX3DComposableVolumeRenderStyle):
    m_strNodeName = "EdgeEnhancementVolumeStyle"
    def __init__(self):
        self.m_strNodeName = "EdgeEnhancementVolumeStyle"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of 4-tuple float results array using RGBA values [0..1] from SFColorRGBA inputOutput field named "edgeColor"
    def getEdgeColor (self):
        pass
    #
    # Assign 4-tuple float array using RGBA values [0..1] to SFColorRGBA inputOutput field named "edgeColor"
    def setEdgeColor (self, color):
        pass

    # Return float result [] from  type inputOutput field named "gradientThreshold"
    def getGradientThreshold (self):
        pass

    # Assign float value [] to  type inputOutput field named "gradientThreshold"
    def setGradientThreshold (self, value):
        pass

    # Return X3DTexture3DNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "surfaceNormals"
    def getSurfaceNormals (self, result):
        pass

    # Assign X3DTexture3DNode value (using a properly typed node) to SFNode inputOutput field named "surfaceNormals"
    def setSurfaceNormals (self, node):
        pass

    # Assign X3DTexture3DNode value (using a properly typed protoInstance)
    def setSurfaceNormals (self, protoInstance):
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
