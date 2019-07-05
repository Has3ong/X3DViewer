from . import *

# ComposedVolumeStyle defines a concrete node interface that extends interface X3DComposableVolumeRenderStyleNode.
class CComposedVolumeStyle(CX3DComposableVolumeRenderStyle):
    m_strNodeName = "ComposedVolumeStyle"
    def __init__(self):
        self.m_strNodeName = "ComposedVolumeStyle"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth

    # Return array of X3DComposableVolumeRenderStyleNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "renderStyle"
    def getRenderStyle (self, result):
        pass

    # Return number of nodes in "renderStyle" array
    def getNumRenderStyle (self):
        pass

    # Assign X3DComposableVolumeRenderStyleNode array (using a properly typed node array) to MFNode inputOutput field named "renderStyle"
    def setRenderStyle1 (self, nodes):
        pass

    # Assign single X3DComposableVolumeRenderStyleNode value (using a properly typed node) as the MFNode array for inputOutput field named "renderStyle"
    def setRenderStyle2 (self, node):
        pass

    # Assign X3DComposableVolumeRenderStyleNode array (using a properly typed protoInstance array) to MFNode inputOutput field named "renderStyle"
    def setRenderStyle3 (self, node):
        pass

    # Assign X3DComposableVolumeRenderStyleNode array (using a properly typed node array) to MFNode inputOutput field named "renderStyle"
    def setRenderStyle4 (self, nodes):
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
