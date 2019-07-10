from . import *

# LineProperties defines a concrete node interface that extends interface X3DAppearanceChildNode.
class CLineProperties(CX3DAppearanceChildNode):
    m_strNodeName = "LineProperties"
    def __init__(self):
        self.m_strNodeName = "LineProperties"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return boolean result from SFBool inputOutput field named "applied"
    def getApplied (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "applied"
    def setApplied (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "linetype"
    def getLinetype (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "linetype"
    def setLinetype (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "linewidthScaleFactor"
    def getLinewidthScaleFactor (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "linewidthScaleFactor"
    def setLinewidthScaleFactor (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return X3DMetadataObject result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "metadata"
    def getMetadata (self):
        pass

    # Assign X3DMetadataObject value (using a properly typed node) to SFNode inputOutput field named "metadata"
    def setMetadata1 (self, node):
        pass

    # Assign X3DMetadataObject value (using a properly typed protoInstance)
    def setMetadata2 (self, protoInstance):
        pass