from . import *

# OpacityMapVolumeStyle defines a concrete node interface that extends interface X3DComposableVolumeRenderStyleNode.
class COpacityMapVolumeStyle(CX3DComposableVolumeRenderStyle):
    m_strNodeName = "OpacityMapVolumeStyle"
    def __init__(self):
        self.m_strNodeName = "OpacityMapVolumeStyle"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return X3DTexture2DNode|X3DTexture3DNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "transferFunction"
    def getTransferFunction (self, result):
        pass

    # Assign X3DTexture2DNode|X3DTexture3DNode value (using a properly typed node) to SFNode inputOutput field named "transferFunction"
    def setTransferFunction1 (self, node):
        pass

    # Assign X3DTexture2DNode|X3DTexture3DNode value (using a properly typed protoInstance)
    def setTransferFunction2 (self, protoInstance):
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