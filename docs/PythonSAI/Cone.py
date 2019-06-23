from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
from . import *

class CCone(CX3DGeometryNode):
    m_strNodeName = "Cone"
    height = 3.0
    bottomRadius = 4.0
    bottom = True
    side = True
    solid = True

    def __init__(self):
        self.m_strNodeName = "Cone"
        self.m_Parent = [None]
        self.children = []
        self.SourceNode = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0
 
        self.height = 3.0
        self.bottomRadius = 4.0
        self.bottom = True
        self.side = True
        self.solid = True

    def getBottomRadius(self):
        return self.bottomRadius

    def setBottomRadius(self, value):
        self.bottomRadius = value

    def getHeight(self):
        return self.height

    def setHeight(self, value):
        self.height = value

    def getBottom(self):
        return self.bottom

    def setBottom(self, value):
        self.bottom = value

    def getSide(self):
        return self.side

    def setSide(self, value):
        self.side = value

    def getSolid(self):
        return self.solid

    def setSolid(self, value):
        self.solid = value

    def getMetadata(self):
        pass
    def setMetadata1(self, node):
        pass
    def setMetadata2(self, protoInstance):
        pass


    def Draw(self):
        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0, 0, self.height)
        angle = 0.0
        
        for angle in range (0, 360) :
            glVertex3f(sin(angle) * self.bottomRadius / 2, cos(angle) * self.bottomRadius / 2, 0)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0,0,0)
        angle = 0.0
        for angle in range(0, 360) :
            glNormal3f(0, -1, 0)
            glVertex3f(sin(angle) * self.bottomRadius / 2, cos(angle) * self.bottomRadius / 2, 0)
        glEnd()

    #def toXMLString(self):

    #def getPropertyString(self):