from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from . import *

# IndexedFaceSet defines a concrete node interface that extends interface X3DComposedGeometryNode.
class CIndexedFaceSet(CX3DComposedGeometryNode):
    m_strNodeName = "IndexedFaceSet"
    
    def __init__(self):
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.coordIndex = []
        self.texCoordIndex = []
        self.creaseAngle = 3.14159265
        self.coord = []
        self.Texturecoord = []
        self.solid = True
        self.ccw = True
        self.depth = 0
        self.n_Count = -1

    # Assign MFInt32 value using RGB values [0..1] to MFInt32 inputOnly field named "set_colorIndex"
    def setColorIndex1 (self, colors, size):
        pass

    # Assign single SFInt32 value using RGB values [0..1] as the MFInt32 array for inputOnly field named "set_colorIndex"
    def setColorIndex2 (self, color):
        pass

    # Assign MFInt32 value [] to MFInt32 inputOnly field named "set_coordIndex"
    def setCoordIndex3 (self, values, size):
        pass

    # Assign single SFInt32 value [] as the MFInt32 array for inputOnly field named "set_coordIndex"
    def setCoordIndex4 (self, value):
        pass

    # Assign MFInt32 value [] to MFInt32 inputOnly field named "set_normalIndex"
    def setNormalIndex1 (self, values, size):
        pass

    # Assign single SFInt32 value [] as the MFInt32 array for inputOnly field named "set_normalIndex"
    def setNormalIndex2 (self, value):
        pass

    # Assign MFInt32 value [] to MFInt32 inputOnly field named "set_texCoordIndex"
    def setTexCoordIndex (self, values, size):
        pass

    # Assign single SFInt32 value [] as the MFInt32 array for inputOnly field named "set_texCoordIndex"
    def setTexCoordIndex (self, value):
        pass

    # Return boolean result from SFBool initializeOnly field named "convex"
    def getConvex (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "convex"
    def setConvex (self, value):
        pass

    # Return float result in radians from  type initializeOnly field named "creaseAngle"
    def getCreaseAngle (self):
        pass

    # Assign float value in radians to  type initializeOnly field named "creaseAngle"
    def setCreaseAngle (self, angle):
        pass

    # Return MFInt32 result using RGB values [0..1] from MFInt32 initializeOnly field named "colorIndex"
    def getColorIndex (self):
        pass

    # Return number of primitive values in "colorIndex" array
    def getNumColorIndex (self):
        pass

    # Assign MFInt32 value using RGB values [0..1] to MFInt32 initializeOnly field named "colorIndex"
    def setColorIndex1 (self, colors, size):
        pass

    # Assign single SFInt32 value using RGB values [0..1] as the MFInt32 array for initializeOnly field named "colorIndex"
    def setColorIndex2 (self, color):
        pass

    # Return MFInt32 result [] from MFInt32 initializeOnly field named "coordIndex"
    def getCoordIndex (self):
        return self.coordIndex

    # Return number of primitive values in "coordIndex" array
    def getNumCoordIndex (self):
        pass

    # Assign MFInt32 value [] to MFInt32 initializeOnly field named "coordIndex"
    def setCoordIndex1 (self, values, size):
        pass

    # Assign single SFInt32 value [] as the MFInt32 array for initializeOnly field named "coordIndex"
    def setCoordIndex2 (self, value):
        pass

    # Return MFInt32 result [] from MFInt32 initializeOnly field named "normalIndex"
    def getNormalIndex (self):
        pass

    # Return number of primitive values in "normalIndex" array
    def getNumNormalIndex (self):
        pass

    # Assign MFInt32 value [] to MFInt32 initializeOnly field named "normalIndex"
    def setNormalIndex1 (self, values, size):
        pass

    # Assign single SFInt32 value [] as the MFInt32 array for initializeOnly field named "normalIndex"
    def setNormalIndex2 (self, value):
        pass

    # Return MFInt32 result [] from MFInt32 initializeOnly field named "texCoordIndex"
    def getTexCoordIndex (self):
        pass

    # Return number of primitive values in "texCoordIndex" array
    def getNumTexCoordIndex (self):
        pass

    # Assign MFInt32 value [] to MFInt32 initializeOnly field named "texCoordIndex"
    def setTexCoordIndex1 (self, values, size):
        pass

    # Assign single SFInt32 value [] as the MFInt32 array for initializeOnly field named "texCoordIndex"
    def setTexCoordIndex2 (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return boolean result from SFBool initializeOnly field named "ccw"
    def getCcw (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "ccw"
    def setCcw (self, value):
        pass

    # Return boolean result from SFBool initializeOnly field named "colorPerVertex"
    def getColorPerVertex (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "colorPerVertex"
    def setColorPerVertex (self, color):
        pass

    # Return boolean result from SFBool initializeOnly field named "normalPerVertex"
    def getNormalPerVertex (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "normalPerVertex"
    def setNormalPerVertex (self, value):
        pass

    # Return boolean result from SFBool initializeOnly field named "solid"
    def getSolid (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "solid"
    def setSolid (self, value):
        pass

    # Return array of X3DVertexAttributeNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "attrib"
    def getAttrib (self, result):
        pass

    # Return number of nodes in "attrib" array
    def getNumAttrib (self):
        pass

    def setAttribute(self, Node):
        self.coordIndex = Node.coordIndex
        self.texCoordIndex = Node.texCoordIndex

    # Assign X3DVertexAttributeNode array (using a properly typed node array) to MFNode inputOutput field named "attrib"
    def setAttrib1 (self, nodes):
        pass

    # Assign single X3DVertexAttributeNode value (using a properly typed node) as the MFNode array for inputOutput field named "attrib"
    def setAttrib2 (self, node):
        pass

    # Assign X3DVertexAttributeNode array (using a properly typed protoInstance array) to MFNode inputOutput field named "attrib"
    def setAttrib3 (self, node):
        pass

    # Assign X3DVertexAttributeNode array (using a properly typed node array) to MFNode inputOutput field named "attrib"
    def setAttrib4 (self, nodes):
        pass

    # Return X3DColorNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "color"
    def getColor (self, result):
        pass

    # Assign X3DColorNode value (using a properly typed node) to SFNode inputOutput field named "color"
    def setColo1r (self, color):
        pass

    # Assign X3DColorNode value (using a properly typed protoInstance)
    def setColo2r (self, protoInstance):
        pass

    # Return X3DCoordinateNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "coord"
    def getCoord (self, result):
        pass

    # Assign X3DCoordinateNode value (using a properly typed node) to SFNode inputOutput field named "coord"
    def setCoord(self, Node):
        self.coord = Node.point

    def setCoord1 (self, node):
        pass

    # Assign X3DCoordinateNode value (using a properly typed protoInstance)
    def setCoord2 (self, protoInstance):
        pass

    # Return FogCoordinate result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "fogCoord"
    def getFogCoord (self, result):
        pass

    # Assign FogCoordinate value (using a properly typed node) to SFNode inputOutput field named "fogCoord"
    def setFogCoord1 (self, node):
        pass

    # Assign FogCoordinate value (using a properly typed protoInstance)
    def setFogCoord2 (self, protoInstance):
        pass

    # Return X3DNormalNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "normal"
    def getNormal (self, result):
        pass

    # Assign X3DNormalNode value (using a properly typed node) to SFNode inputOutput field named "normal"
    def setNormal1 (self, node):
        pass

    # Assign X3DNormalNode value (using a properly typed protoInstance)
    def setNormal2 (self, protoInstance):
        pass

    # Return X3DTextureCoordinateNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "texCoord"
    def getTexCoord (self, result):
        pass

    def setTextureCoord(self, Node):
        self.Texturecoord = Node.point

    # Assign X3DTextureCoordinateNode value (using a properly typed node) to SFNode inputOutput field named "texCoord"
    def setTexCoord1 (self, node):
        pass

    # Assign X3DTextureCoordinateNode value (using a properly typed protoInstance)
    def setTexCoord2 (self, protoInstance):
        pass

    # Return X3DMetadataObject result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "metadata"
    def getMetadata (self):
        pass

    # Assign X3DMetadataObject value (using a properly typed node) to SFNode inputOutput field named "metadata"
    def setMetadata1 (self, node):
        pass

    # Assign X3DMetadataObject value (using a properly typed protoInstance)
    def setMetadata2 (self, protoInstance):
        pass

    def setCCW(self, value):
        pass

    def getCCW(self):
        pass

    def Draw(self):
        i = 0
        length = len(self.coordIndex)

        while 1:
            if i >= length:
                break

            if self.coordIndex[i] ==  'QUAD':
                glBegin(GL_QUADS)
                for j in range (1, 5):
                    if self.texCoordIndex :
                        tindex = self.texCoordIndex[i + j]
                        glTexCoord2f(
                            self.Texturecoord[tindex * 2],
                            self.Texturecoord[tindex * 2 + 1]
                        )          

                    index = self.coordIndex[i + j]
                    glVertex3f(
                        self.coord[index * 3],
                        self.coord[index * 3 + 1],
                        self.coord[index * 3 + 2]
                    )
                glEnd()
                i += 5

            elif self.coordIndex[i] ==  'TRIANGLE':
                glBegin(GL_TRIANGLES)
                for j in range (1, 4):
                    if self.texCoordIndex :
                        tindex = self.texCoordIndex[i + j]
                        glTexCoord2f(
                            self.Texturecoord[tindex * 2],
                            self.Texturecoord[tindex * 2 + 1]
                        )

                    index = self.coordIndex[i + j]
                    glVertex3f(
                        self.coord[index * 3],
                        self.coord[index * 3 + 1],
                        self.coord[index * 3 + 2]
                    )
                glEnd()
                i += 4
            else:
                return 0

    def setCoordIndex(self, strData):
        strSearch = " "
        strSearch2 = "-"
        
        nDelimiter = strData.find("coordIndex")
        strData = strData[nDelimiter + 12:]

        nDelimiter = strData.find("'")
        strData = strData[:nDelimiter]

        while 1:
            tmp_index_1 = 0
            tmp_index_2 = 0
            tmp_index_3 = 0
            tmp_index_4 = 0

            strValue_1 = strData.find(strSearch2)
            t_strData = strData[0 : strValue_1]

            cnt = t_strData.count(" ")

            if cnt == 4 :
                strValue_2 = t_strData.find(strSearch)
                tmp_index_1 = t_strData[0 : strValue_2]
                t_strData = t_strData[strValue_2 + 1 : ]

                strValue_2 = t_strData.find(strSearch)
                tmp_index_2 = t_strData[0 : strValue_2]
                t_strData = t_strData[strValue_2 + 1 : ]

                strValue_2 = t_strData.find(strSearch)
                tmp_index_3 = t_strData[0 : strValue_2]
                t_strData = t_strData[strValue_2 + 1 : ]

                strValue_2 = t_strData.find(strSearch)
                tmp_index_4 = t_strData[0 : strValue_2]

                index_1 = int(tmp_index_1)
                index_2 = int(tmp_index_2)
                index_3 = int(tmp_index_3)
                index_4 = int(tmp_index_4)

                self.coordIndex.append('QUAD')
                self.coordIndex.append(index_1)
                self.coordIndex.append(index_2)
                self.coordIndex.append(index_3)
                self.coordIndex.append(index_4)

            elif cnt == 3 :
                strValue_2 = t_strData.find(strSearch)
                tmp_index_1 = t_strData[0 : strValue_2]
                t_strData = t_strData[strValue_2 + 1 : ]

                strValue_2 = t_strData.find(strSearch)
                tmp_index_2 = t_strData[0 : strValue_2]
                t_strData = t_strData[strValue_2 + 1 : ]

                strValue_2 = t_strData.find(strSearch)
                tmp_index_3 = t_strData[0 : strValue_2]

                index_1 = int(tmp_index_1)
                index_2 = int(tmp_index_2)
                index_3 = int(tmp_index_3)

                self.coordIndex.append('TRIANGLE')
                self.coordIndex.append(index_1)
                self.coordIndex.append(index_2)
                self.coordIndex.append(index_3)

            else :
                break
            strData = strData[strValue_1 +3 : ]

    def setTreeViewCoordIndex(self, value):
        print(value)

    def setTexCoordIndex(self, strData):
        strSearch = " "
        strSearch2 = "-"
        
        nDelimiter = strData.find("texCoordIndex")
        strData = strData[nDelimiter + 15:]

        nDelimiter = strData.find("'")
        strData = strData[:nDelimiter]

        while 1:
            tmp_index_1 = 0
            tmp_index_2 = 0
            tmp_index_3 = 0
            tmp_index_4 = 0

            strValue_1 = strData.find(strSearch2)
            t_strData = strData[0 : strValue_1]

            cnt = t_strData.count(" ")

            if cnt == 4 :
                strValue_2 = t_strData.find(strSearch)
                tmp_index_1 = t_strData[0 : strValue_2]
                t_strData = t_strData[strValue_2 + 1 : ]

                strValue_2 = t_strData.find(strSearch)
                tmp_index_2 = t_strData[0 : strValue_2]
                t_strData = t_strData[strValue_2 + 1 : ]

                strValue_2 = t_strData.find(strSearch)
                tmp_index_3 = t_strData[0 : strValue_2]
                t_strData = t_strData[strValue_2 + 1 : ]

                strValue_2 = t_strData.find(strSearch)
                tmp_index_4 = t_strData[0 : strValue_2]

                index_1 = int(tmp_index_1)
                index_2 = int(tmp_index_2)
                index_3 = int(tmp_index_3)
                index_4 = int(tmp_index_4)

                self.texCoordIndex.append('QUAD')
                self.texCoordIndex.append(index_1)
                self.texCoordIndex.append(index_2)
                self.texCoordIndex.append(index_3)
                self.texCoordIndex.append(index_4)

            elif cnt == 3 :
                strValue_2 = t_strData.find(strSearch)
                tmp_index_1 = t_strData[0 : strValue_2]
                t_strData = t_strData[strValue_2 + 1 : ]

                strValue_2 = t_strData.find(strSearch)
                tmp_index_2 = t_strData[0 : strValue_2]
                t_strData = t_strData[strValue_2 + 1 : ]

                strValue_2 = t_strData.find(strSearch)
                tmp_index_3 = t_strData[0 : strValue_2]

                index_1 = int(tmp_index_1)
                index_2 = int(tmp_index_2)
                index_3 = int(tmp_index_3)

                self.texCoordIndex.append('TRIANGLE')
                self.texCoordIndex.append(index_1)
                self.texCoordIndex.append(index_2)
                self.texCoordIndex.append(index_3)

            else :
                break
            strData = strData[strValue_1 +3 : ]