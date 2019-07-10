from . import *

# FillProperties defines a concrete node interface that extends interface X3DAppearanceChildNode.
class CFillProperties(CX3DAppearanceChildNode):
    m_strNodeName = "FillProperties"
    def __init__(self):
        self.m_strNodeName = "FillProperties"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return boolean result from SFBool inputOutput field named "filled"
    def getFilled (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "filled"
    def setFilled (self, value):
        pass

    # Return boolean result from SFBool inputOutput field named "hatched"
    def getHatched (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "hatched"
    def setHatched (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "hatchStyle"
    def getHatchStyle (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "hatchStyle"
    def setHatchStyle (self, value):
        pass

    # Return array of 3-tuple float results array using RGB values [0..1] from SFColor inputOutput field named "hatchColor"
    def getHatchColor (self, result):
        pass

    # Assign 3-tuple float array using RGB values [0..1] to SFColor inputOutput field named "hatchColor"
    def setHatchColor (self, color):
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
