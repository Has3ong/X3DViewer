from . import *

# SilhouetteEnhancementVolumeStyle defines a concrete node interface that extends interface X3DComposableVolumeRenderStyleNode.
class CSilhouetteEnhancementVolumeStyle(CX3DComposableVolumeRenderStyle):
    m_strNodeName = "SilhouetteEnhancementVolumeStyle"
    def __init__(self):
        self.m_strNodeName = "SilhouetteEnhancementVolumeStyle"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return float result [] from  type inputOutput field named "silhouetteBoundaryOpacity"
    def getSilhouetteBoundaryOpacity (self):
        pass

    # Assign float value [] to  type inputOutput field named "silhouetteBoundaryOpacity"
    def setSilhouetteBoundaryOpacity (self, value):
        pass

    # Return float result [] from  type inputOutput field named "silhouetteRetainedOpacity"
    def getSilhouetteRetainedOpacity (self):
        pass

    # Assign float value [] to  type inputOutput field named "silhouetteRetainedOpacity"
    def setSilhouetteRetainedOpacity (self, value):
        pass

    # Return float result [] from  type inputOutput field named "silhouetteSharpness"
    def getSilhouetteSharpness (self):
        pass

    # Assign float value [] to  type inputOutput field named "silhouetteSharpness"
    def setSilhouetteSharpness (self, value):
        pass

    # Return X3DTexture3DNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "surfaceNormals"
    def getSurfaceNormals (self, result):
        pass

    # Assign X3DTexture3DNode value (using a properly typed node) to SFNode inputOutput field named "surfaceNormals"
    def setSurfaceNormals1 (self, node):
        pass

    # Assign X3DTexture3DNode value (using a properly typed protoInstance)
    def setSurfaceNormals2 (self, protoInstance):
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
