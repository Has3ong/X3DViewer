from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
from . import *

# Cone defines a concrete node interface that extends interface X3DGeometryNode.
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

    # Return float result [] from  type initializeOnly field named "bottomRadius"
    def getBottomRadius(self):
        return self.bottomRadius

    # Assign float value [] to  type initializeOnly field named "bottomRadius"
    def setBottomRadius(self, value):
        self.bottomRadius = value

    # Return float result [] from  type initializeOnly field named "height"
    def getHeight(self):
        return self.height

    # Assign float value [] to  type initializeOnly field named "height"
    def setHeight(self, value):
        self.height = value

    # Return boolean result from SFBool initializeOnly field named "side"
    def getSide(self):
        return self.side

    # Assign boolean value to SFBool initializeOnly field named "side"
    def setSide(self, value):
        self.side = value

    # Return boolean result from SFBool initializeOnly field named "bottom"
    def getBottom(self):
        return self.bottom

    # Assign boolean value to SFBool initializeOnly field named "bottom"
    def setBottom(self, value):
        self.bottom = value

    # Return boolean result from SFBool initializeOnly field named "solid"
    def getSolid(self):
        return self.solid

    # Assign boolean value to SFBool initializeOnly field named "solid"
    def setSolid(self, value):
        self.solid = value

    # Return X3DMetadataObject result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "metadata"
    def getMetadata(self):
        pass
    # Assign X3DMetadataObject value (using a properly typed node) to SFNode inputOutput field named "metadata"
    def setMetadata1(self, node):
        pass
    # Assign X3DMetadataObject value (using a properly typed protoInstance)
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