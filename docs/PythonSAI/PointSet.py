from . import *

# PointSet defines a concrete node interface that extends interface X3DGeometryNode.
class CPointSet(CX3DGeometryNode):
    m_strNodeName = "PointSet"
    def __init__(self):
        self.m_strNodeName = "PointSet"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of X3DVertexAttributeNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "attrib"
    def getAttrib (self, result):
        pass

    # Return number of nodes in "attrib" array
    def getNumAttrib (self):
        pass

    # Assign X3DVertexAttributeNode array (using a properly typed node array) to MFNode inputOutput field named "attrib"
    def setAttrib1 (self, nodes):
        pass

    # Assign single X3DVertexAttributeNode value (using a properly typed node) as the MFNode array for inputOutput field named "attrib"
    def setAttrib2 (self, node):
        pass

    # Assign X3DVertexAttributeNode array (using a properly typed protoInstance array) to MFNode inputOutput field named "attrib"
    def setAttrib3 (self, node):
        pass

    # Assign X3DVertexAttributeNode array (using a properly typed node array) to MFNode inputOutput field named "attrib"
    def setAttrib4 (self, nodes):
        pass

    # Return X3DColorNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "color"
    def getColor (self, result):
        pass

    # Assign X3DColorNode value (using a properly typed node) to SFNode inputOutput field named "color"
    def setColor1 (self, color):
        pass

    # Assign X3DColorNode value (using a properly typed protoInstance)
    def setColor2 (self, protoInstance):
        pass

    # Return X3DCoordinateNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "coord"
    def getCoord (self, result):
        pass

    # Assign X3DCoordinateNode value (using a properly typed node) to SFNode inputOutput field named "coord"
    def setCoord1 (self, node):
        pass

    # Assign X3DCoordinateNode value (using a properly typed protoInstance)
    def setCoord2 (self, protoInstance):
        pass

    # Return FogCoordinate result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "fogCoord"
    def getFogCoord (self, result):
        pass

    # Assign FogCoordinate value (using a properly typed node) to SFNode inputOutput field named "fogCoord"
    def setFogCoord1 (self, node):
        pass

    # Assign FogCoordinate value (using a properly typed protoInstance)
    def setFogCoord2 (self, protoInstance):
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
