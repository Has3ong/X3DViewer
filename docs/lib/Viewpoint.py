from X3DLib import *

class CViewpoint(CX3DViewpointNode):
    m_strNodeName = "Viewpoint"
    CONST_PI = 3.14159265
    fieldOfView = CONST_PI / 4.0

    #def Draw(self):

    #def toXMLString(self):

    #def getPropertyString(self):

    #def setCenterOfRotation(self, value):

    #def getCenterOfRotation(self):

    def setFieldOfView(self, value):
        self.fieldOfView = value

    def getFieldOfView(self):
        return self.fieldOfView

    #def setPosition(self, value):

    #def getPosition(self):

    #def setPosition1(self, pos):

    #def setPosition2(self, value):