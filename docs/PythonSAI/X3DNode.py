from . import *

# X3DNode defines an abstract node interface.
# All instantiable nodes implement X3DNode, which corresponds to SFNode in the X3D specification.
class CX3DNode(CX3DRootNode):
    m_strNodeName = "X3DNode"
    metadata = ""
    DEF = ""
    USE = ""
    SourceNode = []
    depth = 0
    flag = 1

    def __init__(self):
        self.m_strNodeName = "X3DNode"
        self.metadata = ""
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.flag = 1
        self.depth = 0

    # Return X3DMetadataObject result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "metadata"
    def getMetadata(self):
        return self.metadata

    # Assign X3DMetadataObject value (using a properly typed node) to SFNode inputOutput field named "metadata"
    def setMetadata1(self, node):
        self.metadata = node

    # Assign X3DMetadataObject value (using a properly typed protoInstance)
    def setMetadata2(self, protoInstance):
        self.metadata = protoInstance

    def getDEF(self):
        return self.DEF

    def setDEF(self, strDef):
        self.DEF = strDef

    # Dispose of this node's resources.
    def disposs(self):
        pass

    # Get a field for this node by name.
    def getField(self, name):
        pass

    # Get list of available fields in this node.
    def getFieldDefinitions(self):
        pass

    # Determine if node setup is completed.
    def isRealized(self):
        pass

    # Notify node that setup stage is complete.
    def realize(self):
        pass

    def setUSE(self, value):
        self.USE = value

    def getUSE(self):
        return self.USE
