from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from . import *

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

    def setSolid(self, value):
        self.solid = value

    def getSolid(self):
        return self.solid

    def setCCW(self, value):
        self.ccw = value

    def getCCW(self):
        return self.ccw

    def setcreaseAngle(self, value):
        self.creaseAngle = value
    
    def getcreaseAngle(self):
        return self.creaseAngle

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

    def setCoord(self, Node):
        self.coord = Node.point

    def setTextureCoord(self, Node):
        self.Texturecoord = Node.point

    def setAttribute(self, Node):
        self.coordIndex = Node.coordIndex
        self.texCoordIndex = Node.texCoordIndex
