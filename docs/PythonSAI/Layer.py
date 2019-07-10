from . import *

# Layer defines a concrete node interface that extends interface X3DLayerNode.
class CLayer(CX3DLayerNode):
    m_strNodeName = "Layer"
    def __init__(self):
        self.m_strNodeName = "Layer"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Assign X3DChildNode array (using a properly typed node array) to MFNode inputOnly field named "addChildren"
    def addChildren1 (self, nodes):
        pass

    # Assign single X3DChildNode value (using a properly typed node) as the MFNode array for inputOnly field named "addChildren"
    def addChildren2 (self, node):
        pass

    # Assign X3DChildNode array (using a properly typed protoInstance array) to MFNode inputOnly field named "addChildren"
    def addChildren3 (self, node):
        pass

    # Assign X3DChildNode array (using a properly typed node array) to MFNode inputOnly field named "addChildren"
    def addChildren4 (self, nodes):
        pass

    # Assign X3DChildNode array (using a properly typed node array) to MFNode inputOnly field named "removeChildren"
    def removeChildren1 (self, nodes):
        pass

    # Assign single X3DChildNode value (using a properly typed node) as the MFNode array for inputOnly field named "removeChildren"
    def removeChildren2 (self, node):
        pass

    # Assign X3DChildNode array (using a properly typed protoInstance array) to MFNode inputOnly field named "removeChildren"
    def removeChildren3 (self, node):
        pass

    # Assign X3DChildNode array (using a properly typed node array) to MFNode inputOnly field named "removeChildren"
    def removeChildren4 (self, nodes):
        pass

    # Return array of X3DChildNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "children"
    def getChildren (self, result):
        pass

    # Return number of nodes in "children" array
    def getNumChildren (self):
        pass

    # Assign X3DChildNode array (using a properly typed node array) to MFNode inputOutput field named "children"
    def setChildren1 (self, nodes):
        pass

    # Assign single X3DChildNode value (using a properly typed node) as the MFNode array for inputOutput field named "children"
    def setChildren2 (self, node):
        pass

    # Assign X3DChildNode array (using a properly typed protoInstance array) to MFNode inputOutput field named "children"
    def setChildren3 (self, node):
        pass

    # Assign X3DChildNode array (using a properly typed node array) to MFNode inputOutput field named "children"
    def setChildren4 (self, nodes):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return boolean result from SFBool inputOutput field named "isPickable"
    def getIsPickable (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "isPickable"
    def setIsPickable (self, value):
        pass

    # Return X3DMetadataObject result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "metadata"
    def getMetadata (self):
        pass

    # Assign X3DMetadataObject value (using a properly typed node) to SFNode inputOutput field named "metadata"
    def setMetadata1 (self, node):
        pass

    # Assign X3DMetadataObject value (using a properly typed protoInstance)
    def setMetadata2 (self, protoInstance):
        pass

    # Return X3DViewportNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "viewport"
    def getViewport (self, result):
        pass

    # Assign X3DViewportNode value (using a properly typed node) to SFNode inputOutput field named "viewport"
    def setViewport1 (self, node):
        pass

    # Assign X3DViewportNode value (using a properly typed protoInstance)
    def setViewport2 (self, protoInstance):
        pass
