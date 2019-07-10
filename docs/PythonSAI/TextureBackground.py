from . import *

# TextureBackground defines a concrete node interface that extends interface X3DBackgroundNode.
class CTextureBackground(CX3DBackgroundNode):
    m_strNodeName = "TextureBackground"
    def __init__(self):
        self.m_strNodeName = "TextureBackground"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return X3DTexture2DNode|MultiTexture result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "backTexture"
    def getBackTexture (self, result):
        pass

    # Assign X3DTexture2DNode|MultiTexture value (using a properly typed node) to SFNode inputOutput field named "backTexture"
    def setBackTexture1 (self, node):
        pass

    # Assign X3DTexture2DNode|MultiTexture value (using a properly typed protoInstance)
    def setBackTexture2 (self, protoInstance):
        pass

    # Return X3DTexture2DNode|MultiTexture result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "bottomTexture"
    def getBottomTexture (self, result):
        pass

    # Assign X3DTexture2DNode|MultiTexture value (using a properly typed node) to SFNode inputOutput field named "bottomTexture"
    def setBottomTexture1 (self, node):
        pass

    # Assign X3DTexture2DNode|MultiTexture value (using a properly typed protoInstance)
    def setBottomTexture2 (self, protoInstance):
        pass

    # Return X3DTexture2DNode|MultiTexture result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "frontTexture"
    def getFrontTexture (self, result):
        pass

    # Assign X3DTexture2DNode|MultiTexture value (using a properly typed node) to SFNode inputOutput field named "frontTexture"
    def setFrontTexture1 (self, node):
        pass

    # Assign X3DTexture2DNode|MultiTexture value (using a properly typed protoInstance)
    def setFrontTexture2 (self, protoInstance):
        pass

    # Return X3DTexture2DNode|MultiTexture result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "leftTexture"
    def getLeftTexture (self, result):
        pass

    # Assign X3DTexture2DNode|MultiTexture value (using a properly typed node) to SFNode inputOutput field named "leftTexture"
    def setLeftTexture1 (self, node):
        pass

    # Assign X3DTexture2DNode|MultiTexture value (using a properly typed protoInstance)
    def setLeftTexture2 (self, protoInstance):
        pass

    # Return X3DTexture2DNode|MultiTexture result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "rightTexture"
    def getRightTexture (self, result):
        pass

    # Assign X3DTexture2DNode|MultiTexture value (using a properly typed node) to SFNode inputOutput field named "rightTexture"
    def setRightTexture1 (self, node):
        pass

    # Assign X3DTexture2DNode|MultiTexture value (using a properly typed protoInstance)
    def setRightTexture2 (self, protoInstance):
        pass

    # Return X3DTexture2DNode|MultiTexture result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "topTexture"
    def getTopTexture (self, result):
        pass

    # Assign X3DTexture2DNode|MultiTexture value (using a properly typed node) to SFNode inputOutput field named "topTexture"
    def setTopTexture1 (self, node):
        pass

    # Assign X3DTexture2DNode|MultiTexture value (using a properly typed protoInstance)
    def setTopTexture2 (self, protoInstance):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return array of float results array in radians from MFFloat inputOutput field named "groundAngle"
    def getGroundAngle (self):
        pass

    # Return number of primitive values in "groundAngle" array
    def getNumGroundAngle (self):
        pass

    # Assign float array in radians to MFFloat inputOutput field named "groundAngle"
    def setGroundAngle1 (self, angles, size):
        pass

    # Assign single float value in radians as the MFFloat array for inputOutput field named "groundAngle"
    def setGroundAngle2 (self, angle):
        pass

    # Return array of 3-tuple float results array using RGB values [0..1] from MFColor inputOutput field named "groundColor"
    def getGroundColor (self):
        pass

    # Return number of 3-tuple primitive values in "groundColor" array
    def getNumGroundColor (self):
        pass

    # Assign 3-tuple float array using RGB values [0..1] to MFColor inputOutput field named "groundColor"
    def setGroundColor (self, colors, size):
        pass

    # Return array of float results array in radians from MFFloat inputOutput field named "skyAngle"
    def getSkyAngle (self):
        pass

    # Return number of primitive values in "skyAngle" array
    def getNumSkyAngle (self):
        pass

    # Assign float array in radians to MFFloat inputOutput field named "skyAngle"
    def setSkyAngle1 (self, angles, size):
        pass

    # Assign single float value in radians as the MFFloat array for inputOutput field named "skyAngle"
    def setSkyAngle2 (self, angle):
        pass

    # Return array of 3-tuple float results array using RGB values [0..1] from MFColor inputOutput field named "skyColor"
    def getSkyColor (self):
        pass

    # Return number of 3-tuple primitive values in "skyColor" array
    def getNumSkyColor (self):
        pass

    # Assign 3-tuple float array using RGB values [0..1] to MFColor inputOutput field named "skyColor"
    def setSkyColor (self, colors, size):
        pass

    # Return float result [] from intensityType type inputOutput field named "transparency"
    def getTransparency (self):
        pass

    # Assign float value [] to intensityType type inputOutput field named "transparency"
    def setTransparency (self, value):
        pass

    # Assign boolean value to SFBool inputOnly field named "set_bind"
    def setBind (self, value):
        pass

    # Return double result in seconds from SFTime outputOnly field named "bindTime"
    def getBindTime (self):
        pass

    # Return boolean result from SFBool outputOnly field named "isBound"
    def getIsBound (self):
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
