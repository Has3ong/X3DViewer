from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from . import *

class CBox(CX3DGeometryNode):
    m_strNodeName = "Box"
    size = [2.0, 2.0, 2.0]
    solid = True

    def __init__(self, value = None):
        if value == None:
            self.size = [2.0, 2.0, 2.0]
            self.solid = True

        self.size = [2.0, 2.0, 2.0]
        self.solid = True
        

    def setSize(self, vec):
        self.size[0] = vec.x()
        self.size[1] = vec.y()
    
        self.size[2] = vec.z()
    
    def getSize1(self, value):
        value[0] = self.size[0]
        value[1] = self.size[1]
        value[2] = self.size[2]

    def getSize3(self):
        value = CSFVec3f()
        value.setValue3(self.size[0], self.size[1], self.size[2])

        return value

    def setSolid(self, value):
        self.solid = value

    def getSolid(self):
        return solid
        
    def Draw(self):
        point1 = [self.size[0] / 2.0, self.size[1] / 2.0, self.size[2] / -2.0]
        point2 = [self.size[0] / 2.0, self.size[1] / 2.0, self.size[2] / 2.0]
        point3 = [self.size[0] / 2.0, self.size[1] / -2.0, self.size[2] / 2.0]
        point4 = [self.size[0] / 2.0, self.size[1] / -2.0, self.size[2] / -2.0]
        point5 = [self.size[0] / -2.0, self.size[1] / -2.0, self.size[2] / 2.0]
        point6 = [self.size[0] / -2.0, self.size[1] / 2.0, self.size[2] / 2.0]
        point7 = [self.size[0] / -2.0, self.size[1] / 2.0, self.size[2] / -2.0]
        point8 = [self.size[0] / -2.0, self.size[1] / -2.0, self.size[2] / -2.0]
        
        glBegin(GL_QUADS)

        glVertex3fv(point1) #TOP
        glVertex3fv(point2)
        glVertex3fv(point6)
        glVertex3fv(point7)

        glVertex3fv(point3) #Bottom
        glVertex3fv(point4)
        glVertex3fv(point8)
        glVertex3fv(point5)

        glVertex3fv(point2) #Front
        glVertex3fv(point3)
        glVertex3fv(point5)
        glVertex3fv(point6)

        glVertex3fv(point7) #Back
        glVertex3fv(point8)
        glVertex3fv(point4)
        glVertex3fv(point1)

        glVertex3fv(point6) #Left
        glVertex3fv(point5)
        glVertex3fv(point8)
        glVertex3fv(point7)

        glVertex3fv(point1) #Right
        glVertex3fv(point4)
        glVertex3fv(point3)
        glVertex3fv(point2)

        glEnd()

    #def toXMLString(self):

    #def getPropertyString(self):
