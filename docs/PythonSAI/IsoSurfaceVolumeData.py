from . import *

# IsoSurfaceVolumeData defines a concrete node interface that extends interface X3DVolumeDataNode.
class CIsoSurfaceVolumeData(CX3DVolumeDataNode):
    m_strNodeName = "IsoSurfaceVolumeData"
    def __init__(self):
        self.m_strNodeName = "IsoSurfaceVolumeData"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return float result [] from SFFloat inputOutput field named "contourStepSize"
    def getContourStepSize (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "contourStepSize"
    def setContourStepSize (self, value):
        pass

    # Return float result [] from  type inputOutput field named "surfaceTolerance"
    def getSurfaceTolerance (self):
        pass

    # Assign float value [] to  type inputOutput field named "surfaceTolerance"
    def setSurfaceTolerance (self, value):
        pass

    # Return array of float results array [] from MFFloat inputOutput field named "surfaceValues"
    def getSurfaceValues (self):
        pass

    # Return number of primitive values in "surfaceValues" array
    def getNumSurfaceValues (self):
        pass

    # Assign float array [] to MFFloat inputOutput field named "surfaceValues"
    def setSurfaceValues (self, values, size):
        pass

    # Assign single float value [] as the MFFloat array for inputOutput field named "surfaceValues"
    def setSurfaceValues (selfe, value):
        pass

    # Return array of X3DVolumeRenderStyleNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "renderStyle"
    def getRenderStyle (self, result):
        pass

    # Return number of nodes in "renderStyle" array
    def getNumRenderStyle (self):
        pass

    # Assign X3DVolumeRenderStyleNode array (using a properly typed node array) to MFNode inputOutput field named "renderStyle"
    def setRenderStyle1 (self, nodes):
        pass

    # Assign single X3DVolumeRenderStyleNode value (using a properly typed node) as the MFNode array for inputOutput field named "renderStyle"
    def setRenderStyle2 (self, node):
        pass

    # Assign X3DVolumeRenderStyleNode array (using a properly typed protoInstance array) to MFNode inputOutput field named "renderStyle"
    def setRenderStyle3 (self, node):
        pass

    # Assign X3DVolumeRenderStyleNode array (using a properly typed node array) to MFNode inputOutput field named "renderStyle"
    def setRenderStyle4 (self, nodes):
        pass

    # Return X3DTexture3DNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "gradients"
    def getGradients (self, result):
        pass

    # Assign X3DTexture3DNode value (using a properly typed node) to SFNode inputOutput field named "gradients"
    def setGradients1 (self, node):
        pass

    # Assign X3DTexture3DNode value (using a properly typed protoInstance)
    def setGradients2 (self, protoInstance):
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
