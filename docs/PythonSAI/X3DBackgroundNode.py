from . import *

# X3DBackgroundNode defines an abstract node interface that extends interfaces X3DChildNode, X3DNode.
class CX3DBackgroundNode(CX3DBindableNode):
    m_strNodeName = "X3DBackgroundNode"
    groundAngle = []
    groundColor = []
    skyAngle = []
    skyColor = [1.0, 1.0, 1.0, 0.0]
    transparency = 0.0

    def __init__(self):
        self.m_strNodeName = "X3DBackgroundNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

        self.groundAngle = []
        self.groundColor = []
        self.skyAngle = []
        self.skyColor = [0.0, 0.0, 0.0, 0.0]
        self.transparency = 0.0

    # Return array of float results array in radians from MFFloat inputOutput field named "groundAngle"
    def getGroundAngle(self):
        return self.groundAngle

    # Return number of primitive values in "groundAngle" array
    def getNumGroundAngle(self):
        return len(self.groundAngle)

    # Assign float array in radians to MFFloat inputOutput field named "groundAngle"
    def setGroundAngle1(self, angles, size):
        for i in range(0, size):
            self.groundAngle.append(angles[i])

    # Assign single float value in radians as the MFFloat array for inputOutput field named "groundAngle"
    def setGroundAngle2(self, angle):
        self.groundAngle.append(angle)

    # Return array of 3-tuple float results array using RGB values [0..1] from MFColor inputOutput field named "groundColor"
    def getGroundColor(self):
        return self.groundColor

    # Return number of 3-tuple primitive values in "groundColor" array
    def getNumGroundColor(self):
        return len(self.groundColor)

    # Assign 3-tuple float array using RGB values [0..1] to MFColor inputOutput field named "groundColor"
    def setGroundColor(self, colors, size):
        for i in range(0, size):
            self.groundColor.append(colors[i])

    # Return array of float results array in radians from MFFloat inputOutput field named "skyAngle"
    def getSkyAngle(self):
        return self.skyAngle

    # Return number of primitive values in "skyAngle" array
    def getNumSkyAngle(self):
        return len(self.skyAngle)

    # Assign float array in radians to MFFloat inputOutput field named "skyAngle"
    def setSkyAngle1(self, angles, size):
        for i in range(0, size):
            self.skyAngle.append(angles[i])

    # Assign single float value in radians as the MFFloat array for inputOutput field named "skyAngle"
    def setSkyAngle2(self, angle):
        self.skyAngle.append(angle)

    # Return array of 3-tuple float results array using RGB values [0..1] from MFColor inputOutput field named "skyColor"
    def getSkyColor(self):
        return self.skyColor

    # Return number of 3-tuple primitive values in "skyColor" array
    def getNumSkyColor(self):
        return len(self.skyColor)

    # Assign 3-tuple float array using RGB values [0..1] to MFColor inputOutput field named "skyColor"
    def setSkyColor(self, color, size):
        self.skyColor[0] = color.r()
        self.skyColor[1] = color.g()
        self.skyColor[2] = color.b()

    # Return float result [] from intensityType type inputOutput field named "transparency"
    def getTransparency(self):
        return self.transparency

    # Assign float value [] to intensityType type inputOutput field named "transparency"
    def setTransparency(self, value):
        self.transparency = value

    # ===== methods for fields inherited from parent interfaces =====

    # Assign bool value to SFBool inputOnly field named "set_bind"
    def setBind (self, value):
        pass

    # Return double result in seconds from SFTime outputOnly field named "bindTime"
    def getBindTime (self):
        pass

    # Return bool result from SFBool outputOnly field named "isBound"
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