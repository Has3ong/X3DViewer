from . import *

# X3DParametricGeometryNode defines an abstract node interface that extends interfaces X3DNode.
class CX3DParametricGeometryNode(CX3DGeometryNode):
    m_strNodeName = "X3DParametricGeometryNode"
    def __init__(self):
        self.m_strNodeName = "X3DParametricGeometryNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0
 
    # ===== methods for fields inherited from parent interfaces =====

    # Return X3DMetadataObject result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "metadata"
    def getMetadata(self):
        pass

    # Assign X3DMetadataObject value (using a properly typed node) to SFNode inputOutput field named "metadata"
    def setMetadata1 (self, node):
        pass

    # Assign X3DMetadataObject value (using a properly typed protoInstance)
    def setMetadata2 (self, protoInstance):
        pass