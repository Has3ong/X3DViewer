from X3DLib import *

class CX3DBackgroundNode(CX3DBindableNode):
    m_strNodeName = "X3DBackgroundNode"
    groundAngle = []
    groundColor = []
    skyAngle = []
    skyColor = [1.0, 1.0, 1.0, 0.0]
    transparency = 0.0

    #def Draw(self):

    #def toXMLString(self):

    #def getPropertyString(self):
    
    def setGroundAngle1(self, angle):
        self.groundAngle.append(angle)

    def setGroundAngle2(self, angles, size):
        for i in range(0, size):
            self.groundAngle.append(angles[i])

    def getGroundAngle(self):
        return self.groundAngle

    def getNumGroundAngle(self):
        return len(self.groundAngle)

    def setGroundColor1(self, colors):
        self.groundColor.append(colors)

    def setGroundColor2(self, colors, size):
        for i in range(0, size):
            self.groundColor.append(colors[i])

    def getGroundColor(self):
        return self.groundColor

    def getNumGroundColor(self):
        return len(self.groundColor)

    def setSkyAngle1(self, angle):
        self.skyAngle.append(angle)

    def setSkyAngle2(self, angles, size):
        for i in range(0, size):
            self.skyAngle.append(angles[i])

    def getSkyAngle(self):
        return self.skyAngle

    def getSkyAngle(self):
        return len(self.skyAngle)

    def setSkyColor1(self, colors):
        self.skyColor.append(colors)

    def setSkyColor2(self, colors, size):
        for i in range(0, size):
            self.skyColor.append(colors[i])

    def setSkyColor3(self, color):
        self.skyColor[0] = color.r()
        self.skyColor[1] = color.g()
        self.skyColor[2] = color.b()

    def getSkyColor(self):
        return self.skyColor

    def getSkyColor(self):
        return len(self.skyColor)

    def setTransparency(self, value):
        self.transparency = value

    def getTransparency(self):
        return self.transparency
        