from X3DLib import *

X3D = [
    'head',
    'meta',
    'Inline',
    'body',
    'Scene',
    'Shape',
    'Transform',
    'Viewpoint',
    'Background',
    'Appearance',
    'Material',
    'ImageTexture',
    'Box',
    'Cone',
    'Cylinder',
    'Sphere',
    'Text',
    'IndexedFaceSet',
    'TextureCoordinate',
    'Coordinate',
    'Switch'
]

class CX3DTree():

    filepath = ""

    def __init__(self):
        self.m_pCurrentNode = CX3DRootNode()
        self.m_pCurrentNode.setNodeName("X3D")

    def CreateNode(self, strData, flag):
        nDelimiter = 0
        for element in X3D:
            nDelimiter = strData.find(element)
            if nDelimiter > 0 :
                break

        if element == "Material":
            self.ElementMaterial(strData, flag)

        elif element == "Head":
            self.ElementHead(strData, flag)

        elif element == "Background":
            self.ElementBackground(strData, flag)

        elif element == "Transform":
            self.ElementTransform(strData, flag)

        elif element == "Group":
            self.ElementGroup(strData, flag)

        elif element == "Body":
            self.ElementBody(strData, flag)

        elif element == "Scene":
            self.ElementScene(strData, flag)

        elif element == "Shape":
            self.ElementShape(strData, flag)

        elif element == "Appearance":
            self.ElementAppearance(strData, flag)

        elif element == "Box":
            self.ElementBox(strData, flag)

        elif element == "Cone":
            self.ElementCone(strData, flag)

        elif element == "Cylinder":
            self.ElementCylinder(strData, flag)

        elif element == "Sphere":
            self.ElementSphere(strData, flag)
        
        elif element == "Color":
            self.ElementColor(strData, flag)

        elif element == "Viewpoint":
            self.ElementViewpoint(strData, flag)

        else:
            self.ElementNode(strData, flag)
        '''
        elif element == "Coordinate":
            p = CX3DCoordinateNode()

        elif element == "Normal":
            p = CX3DNormalNode()

        elif element == "IndexedFaceSet":
            p = CX3DIndexedFaceSet()
        '''

    def AddNode(self, pNode, flag):
        if flag == 1:
            current = self.m_pCurrentNode
            pNode.nID = current.nID + 1
            current.addChildren(pNode)

            self.m_pCurrentNode = current
        
        elif flag == 2:
            current = self.m_pCurrentNode
            pNode.nID = current.nID + 1
            current.addChildren(pNode)

            self.m_pCurrentNode = current
            self.m_pCurrentNode = pNode
        else:
            return

    def GetSolid(self, string):
        if string == 'true':
            return True
        else:
            return False

    def GetValue1(self, strValue, Array):
        nDelimiter = 0
        strTemp = ""

        strValue = strValue + " "
        while True:
            nDelimiter = strValue.find(" ")
            if nDelimiter < 0:
                break

            else:
                strTemp = strValue[0 : nDelimiter]
                Array.append(float(strTemp))

    def GetValue3(self, strValue, Vec):
        nDelimiter = 0
        tx = 0.0
        ty = 0.0
        tz = 0.0

        strTemp = ""

        nDelimiter = strValue.find(" ")
        if nDelimiter < 0:
            return False
        strTemp = strValue[0 : nDelimiter]
        tx = float(strTemp)
        strValue = strValue[nDelimiter + 1 : ]

        nDelimiter = strValue.find(" ")
        if nDelimiter < 0 :
            return False
        strTemp = strValue[0 : nDelimiter]
        ty = float(strTemp)
        strValue = strValue[nDelimiter + 1: ]

        tz = float(strTemp)

        Vec.setValue3(tx, ty, tz)

    def GetValue4(self, strValue, Vec):
        nDelimiter = 0
        tx = 0.0
        ty = 0.0
        tz = 0.0
        ta = 0.0

        strTemp = ""

        nDelimiter = strValue.find(" ")
        if nDelimiter < 0:
            return False
        strTemp = strValue[0 : nDelimiter]
        tx = float(strTemp)
        strValue = strValue[nDelimiter + 1 : ]

        nDelimiter = strValue.find(" ")
        if nDelimiter < 0 :
            return False
        strTemp = strValue[0 : nDelimiter]
        ty = float(strTemp)
        strValue = strValue[nDelimiter + 1: ]

        nDelimiter = strValue.find(" ")
        if nDelimiter < 0:
            return False
        strTemp = strValue[0 : nDelimiter]
        tz = float(strTemp)
        strValue = strValue[nDelimiter + 1 : ]

        ta = float(strTemp)

        Vec.setValue4(tx, ty, tz, ta)

    def Lookup(self, Search_strData, strData):
        result = ""
        nDelimiter = 0
        nDelimiter = strData.find(Search_strData)
        if nDelimiter > 0:
            strData = strData[nDelimiter:]
            left = len(Search_strData)
            strData = strData[left+2 : ]

            right = strData.find("'")
            strData = strData[0 : right]

            result = strData
        else :
            return False

        return result

    def ElementHead(self, strData, flag):
        pNode = CHead()
        self.AddNode(pNode, flag)
    def ElementBox(self, strData, flag):
        pNode = CBox()

        string = self.Lookup("solid", strData)
        if string:
            result = self.GetSolid(string)
            if result != True:
                pNode.setSolid(False)

        string = self.Lookup("size", strData)
        if string:
            Vec = CSFVec3f()
            self.GetValue3(string, Vec)
            pNode.setSize(Vec)

        self.AddNode(pNode, flag)

    def ElementCone(self, strData, flag):
        pNode = CCone()

        string = self.Lookup("solid", strData)
        if string:
            result = self.GetSolid(string)
            if result != True:
                pNode.setSolid(False)

        string = self.Lookup("height", strData)
        if string:
            result = float(string)
            pNode.setHeight(result)

        string = self.Lookup("bottomRadius", strData)
        if string:
            result = float(string)
            pNode.setBottomRadius(result)

        string = self.Lookup("bottom", strData)
        if string:
            result = self.GetSolid(string)
            if result != True:
                pNode.setSolid(False)

        string = self.Lookup("side", strData)
        if string:
            result = self.GetSolid(string)
            if result != True:
                pNode.setSolid(False)

        self.AddNode(pNode, flag)
        
    def ElementCylinder(self, strData, flag):
        pNode = CCylinder

        string = self.Lookup("solid", strData)
        if string:
            result = self.GetSolid(string)
            if result != True:
                pNode.setSolid(False)

        string = self.Lookup("height", strData)
        if string:
            result = float(string)
            pNode.setHeight(result)

        string = self.Lookup("radius", strData)
        if string:
            result = float(string)
            pNode.setBottomRadius(result)
        
        string = self.Lookup("bottom", strData)
        if string:
            result = self.GetSolid(string)
            if result != True:
                pNode.setSolid(False)

        string = self.Lookup("side", strData)
        if string:
            result = self.GetSolid(string)
            if result != True:
                pNode.setSolid(False)

        string = self.Lookup("top", strData)
        if string:
            result = self.GetSolid(string)
            if result != True:
                pNode.setSolid(False)

        self.AddNode(pNode, flag)

    def ElementSphere(self, strData, flag):
        pNode = CSphere()

        string = self.Lookup("solid", strData)
        if string:
            result = self.GetSolid(string)
            if result != True:
                pNode.setSolid(False)
        
        string = self.Lookup("radius", strData)
        if string:
            result = float(string)
            pNode.setHeight(result)

        self.AddNode(pNode, flag)

    def ElementMaterial(self, strData, flag):
        pNode = CMaterial()

        string = self.Lookup("radius", strData)
        if string:
            pNode.setDEF(string)

        string = self.Lookup("ambientIntensity", strData)
        if string:
            result = float(string)
            pNode.setAmbientIntensity(result)

        string = self.Lookup("diffuseColor", strData)
        if string:
            cval = CSFColor()
            self.GetValue3(string, cval)
            pNode.setDiffuseColor2(cval)

        string = self.Lookup("emissiveColor", strData)
        if string:
            cval = CSFColor()
            self.GetValue3(string, cval)
            pNode.setEmissiveColor2(cval)

        string = self.Lookup("shininess", strData)
        if string:
            result = float(string)
            pNode.setShininess(result)
            
        string = self.Lookup("specularColor", strData)
        if string:
            cval = CSFColor()
            self.GetValue3(string, cval)
            pNode.setSpecularColor2(cval)

        string = self.Lookup("transparency", strData)
        if string:
            result = float(string)
            pNode.setTransparency(result)

    def ElementBackground(self, strData, flag):
        pNode = CBackground()

        string = self.Lookup("skyColor", strData)
        if string:
            cval = CSFColor()
            self.GetValue3(string, cval)
            pNode.setSkyColor3(cval)

        self.AddNode(pNode, flag)

    def ElementTransform(self, strData, flag):
        pNode = CTransform()

        string = self.Lookup("DEF", strData)
        if string:
            pNode.setDEF(string)

        string = self.Lookup("center", strData)
        if string:
            Vec = CSFVec3f()
            self.GetValue3(string, Vec)
            pNode.setCenter2(Vec)

        string = self.Lookup("rotation", strData)
        if string:
            Vec = CSFVec4f()
            self.GetValue4(string, Vec)
            pNode.setRotation2(Vec)

        string = self.Lookup("scale", strData)
        if string:
            Vec = CSFVec3f()
            self.GetValue3(string, Vec)
            pNode.setScale2(Vec)

        string = self.Lookup("scaleOrientation", strData)
        if string:
            Vec = CSFVec4f()
            self.GetValue4(string, Vec)
            pNode.setScale2(Vec)

        string = self.Lookup("translation", strData)
        if string:
            Vec = CSFVec3f()
            self.GetValue3(string, Vec)
            pNode.setScale2(Vec)

        self.AddNode(pNode, flag)
    
    def ElementGroup(self, strData, flag):
        pNode = CGroup()

        string = self.Lookup("DEF", strData)
        if string:
            pNode.setDEF(string)

        self.AddNode(pNode, flag)

    def ElementBody(self, strData, flag):
        pNode = CBody()

        self.AddNode(pNode, flag)

    def ElementScene(self, strData, flag):
        pNode = CScene()

        self.AddNode(pNode, flag)

    def ElementShape(self, strData, flag):
        pNode = CShape()

        string = self.Lookup("DEF", strData)
        if string:
            pNode.setDEF(string)

        self.AddNode(pNode, flag)

    def ElementAppearance(self, strData, flag):
        pNode = CAppearance()

        string = self.Lookup("DEF", strData)
        if string:
            pNode.setDEF(String)

        self.AddNode(pNode, flag)

    def ElementViewpoint(self, strData, flag):
        pNode = CViewpoint()

        string = self.Lookup("description", strData)
        if string:
            pNode.setDescription(string)

        string = self.Lookup("orientation", strData)
        if string:
            Vec = CSFVec4f()
            self.GetValue4(string, Vec)
            pNode.setOrientation(Vec)

        string = self.Lookup("position", strData)
        if string:
            Vec = CSFVec3f()
            self.GetValue3(string, Vec)
            pNode.setPosition(Vec)

        string = self.Lookup("centerOfRotation", strData)
        if string:
            Vec = CSFVec3f()
            self.GetValue3(string, Vec)
            pNode.setCenterOfRotation(Vec)

        string = self.Lookup("jump", strData)
        if string:
            result = self.GetSolid(string)
            if result != True:
                pNode.setJump(False)

        string = self.Lookup("retainUserOffsets", strData)
        if string:
            result = self.GetSolid(string)
            if result != False:
                pNode.setRetainUserOffsets(True)

        string = self.Lookup("fieldOfView", strData)
        if string:
            result = float(string)
            pNode.setFieldOfView(result)

        self.AddNode(pNode, flag)


    def ElementColor(self, strData, flag):
        pNode = 0
        #pNode = CColor()
        self.AddNode(pNode, flag)

    def ElementNode(self, strData, flag):
        pNode = CX3DNode()
        self.AddNode(pNode, flag)

    def parse(self, filepath):
        self.filepath = filepath

        f = open(filepath)
        strData = ""
        strValue1 = "</"
        strValue2 = "/>"
        strValue3 = "<"
        flag = -1

        while True:
            nDelimiter = 0
            strData = f.readline()

            if not strData:
                break

            # </
            nDelimiter = strData.find(strValue1)
            if nDelimiter > 0 :
                self.m_pCurrentNode = self.m_pCurrentNode.m_Parent
                continue

            # />
            nDelimiter = strData.find(strValue2)
            if nDelimiter > 0 :
                flag = 1
                self.CreateNode(strData, flag)
                continue
    
            # <
            nDelimiter = strData.find(strValue3)
            if nDelimiter > 0 :
                flag = 2
                self.CreateNode(strData, flag)
                continue

    def print_X3D(self, root):
        space = []

        length = len(root.children)

        print(root.m_strNodeName)
        for i in range (0, length):
            print(root.children[i].m_strNodeName)

    




            
