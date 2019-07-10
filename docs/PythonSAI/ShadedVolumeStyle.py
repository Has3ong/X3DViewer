from . import *

# ShadedVolumeStyle defines a concrete node interface that extends interface X3DComposableVolumeRenderStyleNode.
class CShadedVolumeStyle(CX3DComposableVolumeRenderStyle):
    m_strNodeName = "ShadedVolumeStyle"
    def __init__(self):
        self.m_strNodeName = "ShadedVolumeStyle"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return boolean result from SFBool inputOutput field named "lighting"
    def getLighting (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "lighting"
    def setLighting (self, value):
        pass

    # Return boolean result from SFBool inputOutput field named "shadows"
    def getShadows (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "shadows"
    def setShadows (self, value):
        pass

    # Return String result ["Henyey-Greenstein"|"NONE"] from  type initializeOnly field named "phaseFunction"
    def getPhaseFunction (self):
        pass

    # Assign String value ["Henyey-Greenstein"|"NONE"] to  type initializeOnly field named "phaseFunction"
    def setPhaseFunction (self, value):
        pass

    # Return X3DMaterialNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "material"
    def getMaterial (self, result):
        pass

    # Assign X3DMaterialNode value (using a properly typed node) to SFNode inputOutput field named "material"
    def setMaterial1 (self, node):
        pass

    # Assign X3DMaterialNode value (using a properly typed protoInstance)
    def setMaterial2 (self, protoInstance):
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
