from . import *

# Rectangle2D defines a concrete node interface that extends interface X3DGeometryNode.
class CRectangle2D(CX3DGeometryNode):
    m_strNodeName = "Rectangle2D"
    def __init__(self):
        self.m_strNodeName = "Rectangle2D"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0
 
    # Return array of 2-tuple float results array [] from SFVec2f initializeOnly field named "size"
    def getSize (self):
        pass

    # Assign 2-tuple float array [] to SFVec2f initializeOnly field named "size"
    def setSize (self, value):
        pass

    # Return boolean result from SFBool initializeOnly field named "solid"
    def getSolid (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "solid"
    def setSolid (self, value):
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
