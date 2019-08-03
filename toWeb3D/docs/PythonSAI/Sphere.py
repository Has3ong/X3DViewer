from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from . import *

# Sphere defines a concrete node interface that extends interface X3DGeometryNode
class CSphere(CX3DNode):
    m_strNodeName = "Sphere"
    raidus = 1.0
    solid = True

    def __init__(self):
        self.m_strNodeName = "Sphere"
        self.m_Parent = [None]
        self.children = []
        self.SourceNode = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

        self.radius = 1.0
        self.solid = True

    # Return float result [] from  type initializeOnly field named "radius"
    def getRadius(self):
        return self.radius

    # Assign float value [] to  type initializeOnly field named "radius"
    def setRadius(self, value):
        self.radius = value

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