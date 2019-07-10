from . import *

# LayerSet defines a concrete node interface that extends interface X3DNode.
class CLayerSet(CX3DNode):
    m_strNodeName = "LayerSet"
    def __init__(self):
        self.m_strNodeName = "LayerSet"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return int result [] from SFInt32 inputOutput field named "activeLayer"
    def getActiveLayer (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "activeLayer"
    def setActiveLayer (self, value):
        pass

    # Return MFInt32 result [] from MFInt32 inputOutput field named "order"
    def getOrder (self):
        pass

    # Return number of primitive values in "order" array
    def getNumOrder (self):
        pass
    #
    # Assign MFInt32 value [] to MFInt32 inputOutput field named "order"
    def setOrder1 (self, values, size):
        pass

    # Assign single SFInt32 value [] as the MFInt32 array for inputOutput field named "order"
    def setOrder2 (self, value):
        pass

    # Return array of X3DLayerNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "layers"
    def getLayers (self, result):
        pass

    # Return number of nodes in "layers" array
    def getNumLayers (self):
        pass

    # Assign X3DLayerNode array (using a properly typed node array) to MFNode inputOutput field named "layers"
    def setLayers1 (self, nodes):
        pass

    # Assign single X3DLayerNode value (using a properly typed node) as the MFNode array for inputOutput field named "layers"
    def setLayers2 (self, node):
        pass

    # Assign X3DLayerNode array (using a properly typed protoInstance array) to MFNode inputOutput field named "layers"
    def setLayers3 (self, node):
        pass

    # Assign X3DLayerNode array (using a properly typed node array) to MFNode inputOutput field named "layers"
    def setLayers4 (self, nodes):
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