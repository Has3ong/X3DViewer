from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from . import *


# Box defines a concrete node interface that extends interface X3DGeometryNode.
class CBox(CX3DNode):
    m_strNodeName = "Box"
    size = [2.0, 2.0, 2.0]
    solid = True

    def __init__(self):
        self.m_strNodeName = "Box"
        self.m_Parent = [None]
        self.children = []
        self.SourceNode = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

        self.size = [2.0, 2.0, 2.0]
        self.solid = True

    # Return array of 3-tuple float results array [] from SFVec3f initializeOnly field named "size"
    def getSize1(self, value):
        value[0] = self.size[0]
        value[1] = self.size[1]
        value[2] = self.size[2]

    def getSize3(self):
        value = CSFVec3f()
        value.setValue3(self.size[0], self.size[1], self.size[2])

        return value

    # Assign 3-tuple float array [] to SFVec3f initializeOnly field named "size"
    def setSize(self, vec):
        self.size[0] = vec.x()
        self.size[1] = vec.y()
        self.size[2] = vec.z()

    # Return boolean result from SFBool initializeOnly field named "solid"
    def setSolid(self, value):
        self.solid = value

    # Assign boolean value to SFBool initializeOnly field named "solid"
    def getSolid(self):
        return self.solid

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
        point1 = [self.size[0] / 2.0, self.size[1] / 2.0, self.size[2] / -2.0]
        point2 = [self.size[0] / 2.0, self.size[1] / 2.0, self.size[2] / 2.0]
        point3 = [self.size[0] / 2.0, self.size[1] / -2.0, self.size[2] / 2.0]
        point4 = [self.size[0] / 2.0, self.size[1] / -2.0, self.size[2] / -2.0]
        point5 = [self.size[0] / -2.0, self.size[1] / -2.0, self.size[2] / 2.0]
        point6 = [self.size[0] / -2.0, self.size[1] / 2.0, self.size[2] / 2.0]
        point7 = [self.size[0] / -2.0, self.size[1] / 2.0, self.size[2] / -2.0]
        point8 = [self.size[0] / -2.0, self.size[1] / -2.0, self.size[2] / -2.0]

        glBegin(GL_QUADS)

        glVertex3fv(point1)  # TOP
        glVertex3fv(point2)
        glVertex3fv(point6)
        glVertex3fv(point7)

        glVertex3fv(point3)  # Bottom
        glVertex3fv(point4)
        glVertex3fv(point8)
        glVertex3fv(point5)

        glVertex3fv(point2)  # Front
        glVertex3fv(point3)
        glVertex3fv(point5)
        glVertex3fv(point6)

        glVertex3fv(point7)  # Back
        glVertex3fv(point8)
        glVertex3fv(point4)
        glVertex3fv(point1)

        glVertex3fv(point6)  # Left
        glVertex3fv(point5)
        glVertex3fv(point8)
        glVertex3fv(point7)

        glVertex3fv(point1)  # Right
        glVertex3fv(point4)
        glVertex3fv(point3)
        glVertex3fv(point2)

        glEnd()

    # def toXMLString(self):

    # def getPropertyString(self):


class Box(_X3DGeometryNode):
    __name__ = 'Box'
    specificationUrl = 'https://www.web3d.org/documents/specifications/19775-1/V3.3/Part01/components/geometry3D.html#Box'
    tooltip = 'https://www.web3d.org/x3d/tooltips/X3dTooltips.html#Box'
    FIELD_DECLARATIONS = [('DEF', '', 'SFString', 'inputOutput'),
                          ('size', (2, 2, 2), 'SFVec3f', 'initializeOnly'),
                          ('solid', True, 'SFBool', 'initializeOnly'),
                          ('USE', '', 'SFString', 'inputOutput'),
                          ('class_', '', 'SFString', 'inputOutput'),
                          ('IS', None, 'SFNode', 'inputOutput'),
                          ('metadata', None, 'SFNode', 'inputOutput')]

    def __init__(self, DEF='', size=(2, 2, 2), solid=True, USE='', class_='', IS=None, metadata=None):
        # if _DEBUG: print ('... in ConcreteNode Box __init__ calling super.__init__(' + str(DEF) + ',' + str(USE) + ',' + str(class_) + ',' + str(metadata) + ',' + str(IS) + ')')
        super().__init__(DEF, USE, class_, IS, metadata)  # fields for X3DNode only
        self.size = size
        self.solid = solid

        @property  # - - - - - - - - - - - - -
        def size(self):
            return self.__size

        @size.setter
        def size(self, size=None):
            if size == None:
                size = SFVec3f.DEFAULT_VALUE
            isValidSFVec3f(size)
            self.__size = size

        @property  # - - - - - - - - - - - - -
        def solid(self):
            return self.__solid

        @solid.setter
        def solid(self, solid=None):
            if solid == None:
                solid = SFBool.DEFAULT_VALUE
            isValidSFBool(solid)
            self.__solid = solid
