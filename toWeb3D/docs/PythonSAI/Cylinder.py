from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from . import *


# Cylinder defines a concrete node interface that extends interface X3DGeometryNode.
class CCylinder(CX3DNode):
    m_strNodeName = "Cylinder"
    height = 2.0
    radius = 1.0
    top = True
    bottom = True
    side = True
    solid = True

    def __init__(self):
        self.m_strNodeName = "Cylinder"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

        self.height = 2.0
        self.radius = 1.0
        self.top = True
        self.bottom = True
        self.side = True
        self.solid = True

    # Return boolean result from SFBool initializeOnly field named "bottom"
    def getBottom(self):
        return self.bottom

    # Assign boolean value to SFBool initializeOnly field named "bottom"
    def setBottom(self, value):
        self.bottom = value

    # Return float result [] from  type initializeOnly field named "height"
    def getHeight(self):
        return self.height

    # Assign float value [] to  type initializeOnly field named "height"
    def setHeight(self, value):
        self.height = value

    # Return float result [] from  type initializeOnly field named "radius"
    def getRadius(self):
        return self.radius

    # Assign float value [] to  type initializeOnly field named "radius"
    def setRadius(self, value):
        self.radius = value

    # Return boolean result from SFBool initializeOnly field named "side"
    def getSide(self):
        return self.side

    # Assign boolean value to SFBool initializeOnly field named "side"
    def setSide(self, value):
        self.side = value

    # Return boolean result from SFBool initializeOnly field named "top"
    def getTop(self):
        return self.top

    # Assign boolean value to SFBool initializeOnly field named "top"
    def setTop(self, value):
        self.top = value

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
        x = 0.0
        y = 0.0
        angle = 0.0
        angle_stepsize = 0.01
        CONST_PI = 3.14159265

        glBegin(GL_QUAD_STRIP)
        for angle in self.myrange(0.0, 2 * CONST_PI, angle_stepsize):
            x = self.radius * cos(angle)
            y = self.radius * sin(angle)
            glVertex3f(x, y, self.height)
            glVertex3f(x, y, 0.0)

        glVertex3f(self.radius, 0.0, self.height)
        glVertex3f(self.radius, 0.0, 0.0)
        glEnd()

        glBegin(GL_POLYGON)
        angle = 0.0
        for angle in self.myrange(0.0, 2 * CONST_PI, angle_stepsize):
            x = self.radius * cos(angle)
            y = self.radius * sin(angle)
            glVertex3f(x, y, self.height)

        glVertex3f(self.radius, 0.0, self.height)
        glEnd()

        glBegin(GL_POLYGON)
        angle = 0.0
        for angle in self.myrange(0.0, 2 * CONST_PI, angle_stepsize):
            x = self.radius * cos(angle)
            y = self.radius * sin(angle)
            glVertex3f(x, y, 0)

        glVertex3f(self.radius, 0.0, 0)
        glEnd()

    def myrange(self, start, end, step):
        r = start
        while (r < end):
            yield r
            r += step
    # def toXMLString(self):

    # def getPropertyString(self):