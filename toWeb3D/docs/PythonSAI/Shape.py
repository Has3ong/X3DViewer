from . import *

# Shape defines a concrete node interface that extends interface X3DShapeNode.
class CShape(CX3DNode):
    m_strNodeName = "Shape"
    def __init__(self, value = None):
        self.m_strNodeName = "Shape"
        if value == None:
            self.m_Parent = [None]
            self.children = []
            self.DEF = ""
            self.USE = ""
            self.n_Count = -1
        else:
            self.m_Parent = [None]
            self.children = []
            self.DEF = ""
            self.USE = ""
            self.n_Count = -1

    # Return X3DAppearanceNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "appearance"
    def getAppearance (self, result):
        pass

    # Assign X3DAppearanceNode value (using a properly typed node) to SFNode inputOutput field named "appearance"
    def setAppearance1 (self, node):
        pass

    # Assign X3DAppearanceNode value (using a properly typed protoInstance)
    def setAppearance2 (self, protoInstance):
        pass

    # Return X3DGeometryNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "geometry"
    def getGeometry (self, result):
        pass

    # Assign X3DGeometryNode value (using a properly typed node) to SFNode inputOutput field named "geometry"
    def setGeometry1(self, node):
        self.addChildren(node)

    # Assign X3DGeometryNode value (using a properly typed protoInstance)
    def setGeometry2 (self, protoInstance):
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

    # Return X3DMetadataObject result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "metadata"
    def getMetadata (self):
        pass

    # Assign X3DMetadataObject value (using a properly typed node) to SFNode inputOutput field named "metadata"
    def setMetadata1 (self, node):
        pass

    # Assign X3DMetadataObject value (using a properly typed protoInstance)
    def setMetadata2 (self, protoInstance):
        pass

    def setDEF(self, value):
        self.DEF = value

    def getDEF(self):
        return self.DEF