from . import *

# CADFace defines a concrete node interface that extends interfaces X3DProductStructureChildNodeX3DBoundedObject.
class CCADFace(CX3DProductStructureChildNode, CX3DBoundedObject):
    m_strNodeName = "CADFace"
    def __init__(self):
        self.m_strNodeName = "CADFace"
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

    # Return Shape|LOD|Transform result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "shape"
    def getShape (self, result):
        pass

    # Assign Shape|LOD|Transform value (using a properly typed node) to SFNode inputOutput field named "shape"
    def setShape1 (self, node):
        pass

    # Assign Shape|LOD|Transform value (using a properly typed protoInstance)
    def setShape2 (self, protoInstance):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return String result [] from SFString inputOutput field named "name"
    def getName (self):
        pass

    # Assign String value [] to SFString inputOutput field named "name"
    def setName (self, value):
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
