from . import *

# LOD defines a concrete node interface that extends interface X3DGroupingNode.
class CLOD(CX3DGroupingNode):
    m_strNodeName = "LOD"
    def __init__(self):
        self.m_strNodeName = "LOD"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return int result [] from  type outputOnly field named "level_changed"
    def getLevel (self):
        pass

    # Return boolean result from SFBool initializeOnly field named "forceTransitions"
    def getForceTransitions (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "forceTransitions"
    def setForceTransitions (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "center"
    def getCenter (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "center"
    def setCenter (self, value):
        pass

    # Return array of float results array [] from MFFloat initializeOnly field named "range"
    def getRange (self):
        pass

    # Return number of primitive values in "range" array
    def getNumRange (self):
        pass

    # Assign float array [] to MFFloat initializeOnly field named "range"
    def setRange1 (self, values, size):
        pass

    # Assign single float value [] as the MFFloat array for initializeOnly field named "range"
    def setRange2 (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return array of 3-tuple float results array [] from SFVec3f initializeOnly field named "bboxCenter"
    def getBboxCenter (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f initializeOnly field named "bboxCenter"
    def setBboxCenter (self, value):
        pass

    # Return array of 3-tuple float results array [0,âˆž) or âˆ’1 âˆ’1 âˆ’1 from boundingBoxSizeType type initializeOnly field named "bboxSize"
    def getBboxSize (self):
        pass

    # Assign 3-tuple float array [0,âˆž) or âˆ’1 âˆ’1 âˆ’1 to boundingBoxSizeType type initializeOnly field named "bboxSize"
    def setBboxSize (self, value):
        pass

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

    # Return X3DMetadataObject result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "metadata"
    def getMetadata (self):
        pass

    # Assign X3DMetadataObject value (using a properly typed node) to SFNode inputOutput field named "metadata"
    def setMetadata1 (self, node):
        pass

    # Assign X3DMetadataObject value (using a properly typed protoInstance)
    def setMetadata2 (self, protoInstance):
        pass
