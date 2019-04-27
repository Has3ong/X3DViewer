from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from . import *

class CCylinder(CX3DGeometryNode):
    m_strNodeName = "Cylinder" 
    height = 2.0
    radius = 1.0
    top = True
    bottom = True
    side = True
    solid = True

    def __init__(self):
        self.m_Parent = [None]
        self.children = []
        self.SourceNode = []
        self.DEF = ""
        self.USE = ""
        self.height = 2.0
        self.radius = 1.0
        self.top = True
        self.bottom = True
        self.side = True
        self.solid = True
        
    def setRadius(self, value):
        self.radius = value

    def getRadius(self):
        return self.radius

    def setHeight(self, value):
        self.height = value

    def getHeight(self):
        return self.height
    
    def setTop(self, value):
        self.top = value

    def getTop(self):
        return self.top
        
    def setBottom(self, value):
        self.bottom = value

    def getBottom(self):
        return self.bottom

    def setSide(self, value):
        self.side = value

    def getSide(self):
        return self.side

    def setSolid(self, value):
        self.solid = value

    def getSolid(self):
        return self.solid

    def Draw(self):
        x = 0.0
        y = 0.0
        angle = 0.0
        angle_stepsize = 0.01
        CONST_PI = 3.14159265

        glBegin(GL_QUAD_STRIP)
        for angle in self.myrange(0.0, 2 * CONST_PI, angle_stepsize) :
            x = self.radius * cos(angle)
            y = self.radius * sin(angle)
            glVertex3f(x, y, self.height)
            glVertex3f(x, y, 0.0)

        glVertex3f(self.radius, 0.0, self.height)
        glVertex3f(self.radius, 0.0, 0.0)
        glEnd()

        glBegin(GL_POLYGON)
        angle = 0.0
        for angle in self.myrange(0.0, 2 * CONST_PI, angle_stepsize) :
            x = self.radius * cos(angle)
            y = self.radius * sin(angle)
            glVertex3f(x, y, self.height)
        
        glVertex3f(self.radius, 0.0, self.height)
        glEnd()

        glBegin(GL_POLYGON)
        angle = 0.0
        for angle in self.myrange(0.0, 2 * CONST_PI, angle_stepsize) :
            x = self.radius * cos(angle)
            y = self.radius * sin(angle)
            glVertex3f(x, y, 0)
          
        glVertex3f(self.radius, 0.0, 0)
        glEnd()

    def myrange(self, start, end, step) :
        r = start
        while(r < end) :
            yield r
            r += step
    #def toXMLString(self):

    #def getPropertyString(self):