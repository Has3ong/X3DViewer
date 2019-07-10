from . import *

# CoordinateDouble defines a concrete node interface that extends interface X3DCoordinateNode.
class CCoordinateDouble(CX3DCoordinateNode):
    m_strNodeName = "CoordinateDouble"
    def __init__(self):
        self.m_strNodeName = "CoordinateDouble"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of 3-tuple double results array [] from MFVec3d inputOutput field named "point"
    def getPoint (self):
        pass

    # Return number of 3-tuple primitive values in "point" array
    def getNumPoint (self):
        pass

    # Assign 3-tuple double array [] to MFVec3d inputOutput field named "point"
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
