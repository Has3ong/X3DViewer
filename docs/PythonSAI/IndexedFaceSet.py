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
        self.creaseAngle = 3.14159265
        self.coord = []

    def Draw(self):
        i = 0
        length = len(self.coordIndex)

        while 1:
            if i >= length:
                break
            index_1 = 0
            index_2 = 0
            index_3 = 0
            index_4 = 0
            if self.coordIndex[i] ==  'QUAD':
                
                index_1 = self.coordIndex[i + 1]
                index_2 = self.coordIndex[i + 2]
                index_3 = self.coordIndex[i + 3]
                index_4 = self.coordIndex[i + 4]

                glBegin(GL_QUADS)

                glVertex3f(
                    self.coord[index_1 * 3],
                    self.coord[index_1 * 3 + 1],
                    self.coord[index_1 * 3 + 2]
                )
                glVertex3f(
                    self.coord[index_2 * 3],
                    self.coord[index_2 * 3 + 1],
                    self.coord[index_2 * 3 + 2]
                )
                glVertex3f(
                    self.coord[index_3 * 3],
                    self.coord[index_3 * 3 + 1],
                    self.coord[index_3 * 3 + 2]
                )
                glVertex3f(
                    self.coord[index_4 * 3],
                    self.coord[index_4 * 3 + 1],
                    self.coord[index_4 * 3 + 2]
                )
                glEnd()

                i += 5

            elif self.coordIndex[i] ==  'TRIANGLE':
                index_1 = self.coordIndex[i + 1]
                index_2 = self.coordIndex[i + 2]
                index_3 = self.coordIndex[i + 3]

                glBegin(GL_TRIANGLES)

                glVertex3f(
                    self.coord[index_1 * 3],
                    self.coord[index_1 * 3 + 1],
                    self.coord[index_1 * 3 + 2]
                )
                glVertex3f(
                    self.coord[index_2 * 3],
                    self.coord[index_2 * 3 + 1],
                    self.coord[index_2 * 3 + 2]
                )
                glVertex3f(
                    self.coord[index_3 * 3],
                    self.coord[index_3 * 3 + 1],
                    self.coord[index_3 * 3 + 2]
                )
                glEnd()

                i += 4
            else :
                break

    def setcreaseAngle(self, value):
        self.creaseAngle = value
    
    def getcreaseAngle(self):
        return self.creaseAngle

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

    def setCoord(self, Node):
        self.coord = Node.point
