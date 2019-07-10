from . import *

# Normal defines a concrete node interface that extends interface X3DNormalNode.
class CNormal(CX3DNormalNode):
    m_strNodeName = "Normal"
    def __init__(self):
        self.m_strNodeName = "Normal"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of 3-tuple float results array [] from MFVec3f inputOutput field named "vector"
    def getVector (self):
        pass

    # Return number of 3-tuple primitive values in "vector" array
    def getNumVector (self):
        pass

    # Assign 3-tuple float array [] to MFVec3f inputOutput field named "vector"
    def setVector (self, values, size):
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