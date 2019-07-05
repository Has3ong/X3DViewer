from . import *

# CollisionSpace defines a concrete node interface that extends interface X3DNBodyCollisionSpaceNode.
class CCollisionSpace(CX3DNBodyCollisionSpaceNode):
    m_strNodeName = "CollisionSpace"
    def __init__(self):
        self.m_strNodeName = "CollisionSpace"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return boolean result from SFBool inputOutput field named "useGeometry"
    def getUseGeometry (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "useGeometry"
    def setUseGeometry (self, value):
        pass

    # Return array of X3DNBodyCollisionSpaceNode|X3DNBodyCollidableNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "collidables"
    def getCollidables (self, result):
        pass

    # Return number of nodes in "collidables" array
    def getNumCollidables (self):
        pass

    # Assign X3DNBodyCollisionSpaceNode|X3DNBodyCollidableNode array (using a properly typed node array) to MFNode inputOutput field named "collidables"
    def setCollidables1 (self, nodes):
        pass

    # Assign single X3DNode[] value (using a properly typed node) as the MFNode array for inputOutput field named "collidables"
    def setCollidables2 (self, node):
        pass

    # Assign X3DNBodyCollisionSpaceNode|X3DNBodyCollidableNode array (using a properly typed protoInstance array) to MFNode inputOutput field named "collidables"
    def setCollidables3 (self, node):
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

    # Return boolean result from SFBool inputOutput field named "enabled"
    def getEnabled (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "enabled"
    def setEnabled (self, value):
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
