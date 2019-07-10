from . import *

# MultiTextureCoordinate defines a concrete node interface that extends interface X3DTextureCoordinateNode.
class CMultiTextureCoordinate(CX3DTextureCoordinateNode):
    m_strNodeName = "MultiTextureCoordinate"
    def __init__(self):
        self.m_strNodeName = "MultiTextureCoordinate"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of X3DTextureCoordinateNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "texCoord"
    def getTexCoord (self, result):
        pass

    # Return number of nodes in "texCoord" array
    def getNumTexCoord (self):
        pass

    # Assign X3DTextureCoordinateNode array (using a properly typed node array) to MFNode inputOutput field named "texCoord"
    def setTexCoord1 (self, nodes):
        pass

    # Assign single X3DTextureCoordinateNode value (using a properly typed node) as the MFNode array for inputOutput field named "texCoord"
    def setTexCoord2 (self, node):
        pass

    # Assign X3DTextureCoordinateNode array (using a properly typed protoInstance array) to MFNode inputOutput field named "texCoord"
    def setTexCoord3 (self, node):
        pass

    # Assign X3DTextureCoordinateNode array (using a properly typed node array) to MFNode inputOutput field named "texCoord"
    def setTexCoord4 (self, nodes):
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
