from . import *

# CartoonVolumeStyle defines a concrete node interface that extends interface X3DComposableVolumeRenderStyleNode.
class CCartoonVolumeStyle(CX3DComposableVolumeRenderStyle):
    m_strNodeName = "CartoonVolumeStyle"
    def __init__(self):
        self.m_strNodeName = "CartoonVolumeStyle"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return int result using RGB values [0..1] from  type inputOutput field named "colorSteps"
    def getColorSteps (self):
        pass

    # Assign int value using RGB values [0..1] to  type inputOutput field named "colorSteps"
    def setColorSteps (self, color):
        pass

    # Return array of 4-tuple float results array using RGBA values [0..1] from SFColorRGBA inputOutput field named "orthogonalColor"
    def getOrthogonalColor (self, result):
        pass

    # Assign 4-tuple float array using RGBA values [0..1] to SFColorRGBA inputOutput field named "orthogonalColor"
    def setOrthogonalColor (self, color):
        pass

    # Return array of 4-tuple float results array using RGBA values [0..1] from SFColorRGBA inputOutput field named "parallelColor"
    def getParallelColor (self, result):
        pass

    # Assign 4-tuple float array using RGBA values [0..1] to SFColorRGBA inputOutput field named "parallelColor"
    def setParallelColor (self, color):
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
