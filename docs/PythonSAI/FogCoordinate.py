from . import *

# FogCoordinate defines a concrete node interface that extends interface X3DCoordinateNode.
class CFogCoordinate(CX3DGeometricPropertyNode):
    m_strNodeName = "FogCoordinate"
    def __init__(self):
        self.m_strNodeName = "FogCoordinate"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of float results array [] from MFFloat inputOutput field named "depth"
    def getDepth (self):
        pass

    # Return number of primitive values in "depth" array
    def getNumDepth (self):
        pass

    # Assign float array [] to MFFloat inputOutput field named "depth"
    def setDepth1 (self, values, size):
        pass

    # Assign single float value [] as the MFFloat array for inputOutput field named "depth"
    def setDepth2 (self, value):
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
