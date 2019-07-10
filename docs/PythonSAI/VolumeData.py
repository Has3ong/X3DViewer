from . import *

# VolumeData defines a concrete node interface that extends interface X3DVolumeDataNode.
class CVolumeData(CX3DVolumeDataNode):
    m_strNodeName = "VolumeData"
    def __init__(self):
        self.m_strNodeName = "VolumeData"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return X3DVolumeRenderStyleNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "renderStyle"
    def getRenderStyle (self, result):
        pass

    # Assign X3DVolumeRenderStyleNode value (using a properly typed node) to SFNode inputOutput field named "renderStyle"
    def setRenderStyle1 (self, node):
        pass

    # Assign X3DVolumeRenderStyleNode value (using a properly typed protoInstance)
    def setRenderStyle2 (self, protoInstance):
        pass

    # Return X3DTexture3DNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "voxels"
    def getVoxels (self, result):
        pass

    # Assign X3DTexture3DNode value (using a properly typed node) to SFNode inputOutput field named "voxels"
    def setVoxels1 (self, node):
        pass

    # Assign X3DTexture3DNode value (using a properly typed protoInstance)
    def setVoxels2 (self, protoInstance):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "dimensions"
    def getDimensions (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "dimensions"
    def setDimensions (self, value):
        pass

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
