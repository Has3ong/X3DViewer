from . import *

# TextureCoordinate4D defines a concrete node interface that extends interface X3DTextureCoordinateNode.
class CTextureCoordinate4D(CX3DTextureCoordinateNode):
    m_strNodeName = "TextureCoordinate4D"
    def __init__(self):
        self.m_strNodeName = "TextureCoordinate4D"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of 4-tuple float results array [] from MFVec4f inputOutput field named "point"
    def getPoint (self):
        pass

    # Return number of 4-tuple primitive values in "point" array
    def getNumPoint (self):
        pass

    # Assign 4-tuple float array [] to MFVec4f inputOutput field named "point"
    def setPoint (self, values, size):
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
