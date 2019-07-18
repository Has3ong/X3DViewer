from . import *

# X3DProductStructureChildNode defines an abstract node interface that extends interfaces X3DNode.
# The X3DProductStructureChildNode abstract node type marks nodes that are valid product structure children for the CADInterchange component.
class CX3DProductStructureChildNode(CX3DChildNode):
    m_strNodeName = "X3DProductStructureChildNode"
    def __init__(self):
        self.m_strNodeName = "X3DProductStructureChildNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return String result [] from SFString inputOutput field named "name"
    def getName (self):
        pass

    # Assign String value [] to SFString inputOutput field named "name"
    def setName (self, value):
        pass

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