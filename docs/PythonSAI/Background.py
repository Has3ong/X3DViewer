from . import *

# Background defines a concrete node interface that extends interface X3DBackgroundNode.
class CBackground(CX3DBackgroundNode):
    m_strNodeName = "Background"
    def __init__(self):
        self.m_Parent = [None]
        self.children = []
        self.depth = 0
        self.skyColor = [0.0, 0.0, 0.0]
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

    #Return array of String results array [] from MFString inputOutput field named "backUrl"
    def getBackUrl (self):
        pass

    # Return number of primitive values in "backUrl" array
    def getNumBackUrl (self):
        pass

    # Assign String array [] to MFString inputOutput field named "backUrl"
    def setBackUrl1 (self, values, size):
        pass

    # Assign single String value [] as the MFString array for inputOutput field named "backUrl"
    def setBackUrl2 (self, value):
       pass

    # Return array of String results array [] from MFString inputOutput field named "bottomUrl"
    def getBottomUrl (self):
        pass

    # Return number of primitive values in "bottomUrl" array
    def getNumBottomUrl (self):
        pass

    # Assign String array [] to MFString inputOutput field named "bottomUrl"
    def setBottomUrl1 (self, values, size):
        pass

    # Assign single String value [] as the MFString array for inputOutput field named "bottomUrl"
    def setBottomUrl2 (self, value):
        pass

    # Return array of String results array [] from MFString inputOutput field named "frontUrl"
    def getFrontUrl (self):
        pass

    # Return number of primitive values in "frontUrl" array
    def getNumFrontUrl (self):
        pass

    # Assign String array [] to MFString inputOutput field named "frontUrl"
    def setFrontUrl1 (self, values, size):
        pass

    # Assign single String value [] as the MFString array for inputOutput field named "frontUrl"
    def setFrontUrl2 (self, value):
        pass

    # Return array of String results array [] from MFString inputOutput field named "leftUrl"
    def getLeftUrl (self):
        pass

    # Return number of primitive values in "leftUrl" array
    def getNumLeftUrl (self):
        pass

    # Assign String array [] to MFString inputOutput field named "leftUrl"
    def setLeftUrl1 (self, values, size):
        pass

    # Assign single String value [] as the MFString array for inputOutput field named "leftUrl"
    def setLeftUrl2 (self, value):
        pass

    # Return array of String results array [] from MFString inputOutput field named "rightUrl"
    def getRightUrl (self):
        pass

    # Return number of primitive values in "rightUrl" array
    def getNumRightUrl (self):
        pass

    # Assign String array [] to MFString inputOutput field named "rightUrl"
    def setRightUrl1 (self, values, size):
        pass

    # Assign single String value [] as the MFString array for inputOutput field named "rightUrl"
    def setRightUrl2 (self, value):
        pass

    # Return array of String results array [] from MFString inputOutput field named "topUrl"
    def getTopUrl (self):
        pass

    # Return number of primitive values in "topUrl" array
    def getNumTopUrl (self):
        pass

    # Assign String array [] to MFString inputOutput field named "topUrl"
    def setTopUrl1 (self, values, size):
        pass

    # Assign single String value [] as the MFString array for inputOutput field named "topUrl"
    def setTopUrl2 (self, value):
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
    def setSkyColor(self, colors, size):
        self.skyColor[0] = colors.r()
        self.skyColor[1] = colors.g()
        self.skyColor[2] = colors.b()

    def getSkyColor(self):
        return self.skyColor

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

    def toX3DString(self):
        data = """%s skyColor='%f %f %f'"""%(
            self.m_strNodeName,  self.skyColor[0], self.skyColor[1], self.skyColor[2]
        )

        return data