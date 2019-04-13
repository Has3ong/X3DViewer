from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from X3DLib import *

class CSphere(CX3DGeometryNode):
    m_strNodeName = "Sphere" 
    raidus = 1.0
    solid = True

    def setRadius(self, value):
        self.radius = value

    def getRadius(self):
        return self.radius

    def setSolid(self, value):
        self.solid = value

    def getSolid(self):
        return self.solid

    def Draw(self):
        CONST_PI = 3.14159265
        lats = 50
        longs = 50

        for i in range (0, lats) :
            lat0 = float( CONST_PI * ( -0.5 + float (i - 1 ) / lats ) )
            z0 = float( sin(lat0) )
            zr0 = float( cos(lat0) )

            lat1 = float ( CONST_PI * ( -0.5 + float (i) / lats ) )
            z1 = float( sin(lat1) )
            zr1 = float( cos(lat1) )

            glBegin(GL_QUAD_STRIP)

            for j in range (0, longs) :
                lng = 2 * CONST_PI * float( j - 1 ) / longs
                x = float ( cos(lng) )
                y = float ( sin(lng) )

                glNormal3f(x * zr0, y * zr0, z0)
                glVertex3f(x * zr0, y * zr0, z0)
                glNormal3f(x * zr1, y * zr1, z1)
                glVertex3f(x * zr1, y * zr1, z1)

            glEnd()

    #def toXMLString(self):

    #def getPropertyString(self):