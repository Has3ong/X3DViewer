from . import *

# StaticGroup defines a concrete node interface that extends interfaces X3DChildNode X3DBoundedObject
# StaticGroup is similar to Group node but does not allow access to children after creation time.

class CStaticGroup(CX3DChildNode, CX3DBoundedObject):
    m_strNodeName = "StaticGroup"
    def __init__(self):
        self.m_strNodeName = "StaticGroup"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

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

    # Return array of X3DChildNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode initializeOnly field named "children"
    def getChildren (self, result):
        pass

    # Return number of nodes in "children" array
    def getNumChildren (self):
        pass

    # Assign X3DChildNode array (using a properly typed node array) to MFNode initializeOnly field named "children"
    def setChildren1 (self, nodes):
        pass

    # Assign single X3DChildNode value (using a properly typed node) as the MFNode array for initializeOnly field named "children"
    def setChildren2 (self, node):
        pass

    # Assign X3DChildNode array (using a properly typed protoInstance array) to MFNode initializeOnly field named "children"
    def setChildren3 (self, node):
        pass

    # Assign X3DChildNode array (using a properly typed node array) to MFNode initializeOnly field named "children"
    def setChildren4 (self, nodes):
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
