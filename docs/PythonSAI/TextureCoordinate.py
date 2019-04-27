from . import *

class CTextureCoordinate(CX3DTextureCoordinateNode):
    m_strNodeName = "TextureCoordinate"

    def __init__(self):
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.point = []

<<<<<<< HEAD
    def setPoint(self, strData):
        index = strData.find('point')
        strData = strData[index : ]

        index = strData.find("'")
        strData = strData[index + 1:]

        while 1:  
            strSearch = " "
            strValue = strData.find(strSearch)
            if strValue == -1 :
                length = len(strData)
                t_point = strData[0:length - 4]

                point = float(t_point)

                self.point.append(point)
                break
            else :
                t_point = strData[0 : strValue]

                strData = strData[strValue + 1 :]

                point = float(t_point)
                self.point.append(point)
                
=======
>>>>>>> b70295ed96e87dc8cfa7c28be7a5ebc6c46838f2
    def setAttribute(self, Node):
        self.point = Node.point