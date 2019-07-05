from . import *

# Color defines a concrete node interface that extends interface X3DColorNode.
class CColor(CX3DColorNode):
    m_strNodeName = "Color"
    def __init__(self):
        self.m_strNodeName = "Color"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of 3-tuple float results array using RGB values [0..1] from MFColor inputOutput field named "color"
    def getColor (self):
        pass

    # Return number of 3-tuple primitive values in "color" array
    def getNumColor (self):
        pass

    # Assign 3-tuple float array using RGB values [0..1] to MFColor inputOutput field named "color"
    def setColor (self, colors, size):
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
