from . import *

# TextureCoordinate defines a concrete node interface that extends interface X3DTextureCoordinateNode.
class CTextureCoordinate(CX3DTextureCoordinateNode):
    m_strNodeName = "TextureCoordinate"
    point = []
    def __init__(self):
        self.m_strNodeName = "TextureCoordinate"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0
 
        self.point = []

    # Return array of 2-tuple float results array [] from MFVec2f inputOutput field named "point"
    def getPoint (self):
        pass

    # Return number of 2-tuple primitive values in "point" array
    def getNumPoint (self):
        pass

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
                
    def setAttribute(self, Node):
        self.point = Node.point

    # ===== methods for fields inherited from parent interfaces =====

    # Return X3DMetadataObject result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "metadata"
    def getMetadata (self):
        pass

    # Assign X3DMetadataObject value (using a properly typed node) to SFNode inputOutput field named "metadata"
    def setMetadata1 (self, node):
        pass

    # Assign X3DMetadataObject value (using a properly typed protoInstance)
    def setMetadata2 (self, protoInstance):
        pass
