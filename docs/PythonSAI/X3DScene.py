from . import *

X3D = [
    'head',
    'meta',
    'Inline',
    'Script',
    'field',
    'ROUTE',
    'body',
    'Scene',
    'Shape',
    'Group',
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
    'TouchSensor',
    'IndexedFaceSet',
    'ImageTexture',
    'TextureCoordinate',
    'Coordinate',
    'Text',
    'Switch'
]

class CX3DScene(CX3DNode):
    filepath = ""
    m_strNodeName = "Scene"
    DEF = ""

    m_Node = []
    m_TextureNode = []
    m_ROUTE = []

    m_fields = CFieldArray()
    m_TouchSensor = CTouchSensor()
    m_Script = CScript()
    m_Scene = CScene()
    m_X3DScene = CX3DRootNode()

    def Draw(self):
        pNode = CX3DScene.m_X3DScene
        length = len(CX3DScene.m_X3DScene.children)

        for i in range(0,length):
            self.DrawNode(pNode)
    
    def DrawNode(self, pNode):
        glPushMatrix()

        if pNode.m_strNodeName == "Shape":
            length = len(pNode.children)
            for i in range (0, length):
                if pNode.children[i].m_strNodeName == "Appearance":
                    pChild = pNode.children[i]
                    self.DrawNode(pChild)

        if pNode.m_strNodeName in[
            "Box", "Cone","Cylinder",
            "Sphere", "IndexedFaceSet", "Material",
            "ImageTexture"]:
            pNode.Draw()

        if pNode.m_strNodeName in["Background"]:
            glClearColor(
                pNode.skyColor[0],
                pNode.skyColor[1],
                pNode.skyColor[2],
                0.0
                )

        elif pNode.m_strNodeName in["Viewpoint"]:
            glPushMatrix()
            glTranslatef(
                pNode.position[0],
                pNode.position[1],
                pNode.position[2]
            )
            glRotatef(
                pNode.orientation[0] / 3.14159265 * 180.0,
                pNode.orientation[1],
                pNode.orientation[2],
                pNode.orientation[3]
            )
            glPopMatrix()

        elif pNode.m_strNodeName in["Transform"]:
            glPushMatrix()

            glTranslatef(
                pNode.translation[0],
                pNode.translation[1],
                pNode.translation[2]               
            )
            glScalef(
                pNode.scale[0],
                pNode.scale[1],
                pNode.scale[2]
            )
            glRotatef(
                pNode.rotation[0] / 3.14159265 * 180.0,
                pNode.rotation[1],
                pNode.rotation[2],
                pNode.rotation[3]
            )

            length = len(pNode.children)
            for i in range (0, length):
                pChild = pNode.children[i]
                self.DrawNode(pChild)

            glPopMatrix()

        else :
            glPushMatrix()

            length = len(pNode.children)
            for i in range (0, length):
                pChild = pNode.children[i]
                self.DrawNode(pChild)

            glPopMatrix()

        glPopMatrix()

    #def setFromNode(self, head, cur, value):

    def AddLocation(self, head, fromField, fromNode, toNode):
        if head.DEF == fromNode:
            n_length = len(self.m_Node)
            for i in range(0, n_length):
                if self.m_Node[i].DEF == toNode:
                    head.setToNode(self.m_Node[i])
                    head.setField(self.m_fields.get(fromField))

        length = len(head.children)
        for i in range(0, length):
            self.AddLocation(head.children[i], fromField, fromNode, toNode)

    def Initialize(self, p_head):
        if p_head.m_strNodeName == "ROUTE":
            if p_head.fromNode:
                head = CX3DScene.m_X3DScene
                self.AddLocation(head, p_head.fromField, p_head.fromNode, p_head.toNode)

        if p_head.USE:
            m_length = len(self.m_Node)
            for i in range(0, m_length):
                if p_head.USE == self.m_Node[i].DEF:
                    p_head.setAttribute(self.m_Node[i])

        if p_head.m_strNodeName == "Coordinate":
            p_head.m_Parent[0].setCoord(p_head)
        if p_head.m_strNodeName == "TextureCoordinate":
            p_head.m_Parent[0].setTextureCoord(p_head)

        length = len(p_head.children)
        for i in range(0, length):
            self.Initialize(p_head.children[i])

    def Init(self):
        head = CX3DScene.m_X3DScene
        length = len(head.children)

        for i in range(0, length):
            self.Initialize(head.children[i])

    def Parsing(self, filepath):
        CX3DScene.m_TextureNode.clear()
        CX3DScene.m_X3DScene.init()
        self.m_Node.clear()
        self.m_TextureNode.clear()

        X3DTree = CX3DTree()
        X3DTree.X3D_parse(filepath)
        CX3DScene.m_X3DScene = X3DTree.m_Node
        self.Init()

    def createNode(self, value):
        if value == "Box":
            pNode = CBox()
            return pNode

        elif value == "Shape":
            pNode = CShape()
            return pNode

        elif value == "Group":
            pNode = CGroup()
            return pNode

        elif value == "TouchSensor":
            pNode = CTouchSensor()
            return pNode

    def getNode(self, value):
         length = len(self.m_fields.m_values)
         for i in range (0, length):
             if value == self.m_fields.m_values[i].DEF:
                 return self.m_fields.m_values[i]
    
    def addRoute(self, pSNode, strSField, pDNode, strDField):
        pass

    #def toXMLString(self):

    #def getPropertyString(self):

class CX3DTree():

    m_Node = CX3DRootNode()
    m_SourceNode = []
    
    def __init__(self):
        CX3DTree.m_Node.setNodeName("X3D")
        self.depth = 0

    def CreateNode(self, strData, flag):
        nDelimiter = 0
        for element in X3D:
            nDelimiter = strData.find(element)
            if nDelimiter > 0 :
                break

        if element == "Material":
            self.ElementMaterial(strData, flag)

        elif element == "head":
            self.ElementHead(strData, flag)

        elif element == "Background":
            self.ElementBackground(strData, flag)

        elif element == "Script":
            self.ElementScript(strData, flag)

        elif element == "field":
            self.ElementField(strData, flag)

        elif element == "ROUTE":
            self.ElementROUTE(strData, flag)

        elif element == "Transform":
            self.ElementTransform(strData, flag)

        elif element == "Group":
            self.ElementGroup(strData, flag)

        elif element == "meta":
            self.ElementMeta(strData, flag)

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

        elif element == "TouchSensor":
            self.ElementTouchSensor(strData, flag)
        
        elif element == "Color":
            self.ElementColor(strData, flag)

        elif element == "Viewpoint":
            self.ElementViewpoint(strData, flag)

        elif element == "TextureCoordinate":
            self.ElementTextureCoordinate(strData, flag)

        elif element == "Coordinate":
            self.ElementCoordinate(strData, flag)

        elif element == "Normal":
            self.ElementNormal(strData, flag)

        elif element == "IndexedFaceSet":
            self.ElementIndexedFaceSet(strData, flag)
        
        elif element == "ImageTexture":
            self.ElementImageTexture(strData, flag)
        else:
            self.ElementNode(strData, flag)

    def AddNode(self, pNode, flag):
        if flag == 1:
            CX3DTree.m_Node.addChildren(pNode)
            
        elif flag == 2:
            CX3DTree.m_Node.addChildren(pNode)
            index = CX3DTree.m_Node.n_Count
            CX3DTree.m_Node = CX3DTree.m_Node.children[index]

    def AddSourceNode(self, pNode):
        CX3DTree.m_SourceNode.append(pNode)

    def getSourceNode(self, string, pNode):
        length = len(m_SourceNode)

        for i in range(0, length):
            value = CX3DTree.m_Node[i].getDEF
            if string == value:
                pNode.setSourceNode(CX3DTree.m_Node[i])
                break

    def GetSolid(self, string):
        if string == 'true':
            return True
        else:
            return False
        
    def GetString(self, string, Array):
        nDelimiter = 0
        strTemp = ""
        strValue = string

        nDelimiter = strValue.find("'")
        if nDelimiter > 0:
            strValue = strValue[nDelimiter+1:]
            nDelimiter = strValue.find("'")

            if nDelimiter > 0:
                strValue = strValue[:nDelimiter-1]
                Array.append(strValue)

            else:
                return False

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

        tz = float(strValue)

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

        ta = float(strValue)

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

    def ElementMeta(self, strData, flag):
        pNode = CMeta()

        string = self.Lookup("content", strData)
        if string:
            pNode.setContent(string)

        string = self.Lookup("name", strData)
        if string:
            pNode.setName(string)

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

        string = self.Lookup("DEF", strData)
        if string:
            pNode.setDEF(string)
            CX3DScene.m_Node.append(pNode)

        string = self.Lookup("USE", strData)
        if string:
            pNode.setUSE(string)
            
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

        string = self.Lookup("DEF", strData)
        if string:
            pNode.setDEF(string)
            CX3DScene.m_Node.append(pNode)

        string = self.Lookup("USE", strData)
        if string:
            pNode.setUSE(string)

        self.AddNode(pNode, flag)
        
    def ElementCylinder(self, strData, flag):
        pNode = CCylinder()

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
            pNode.setRadius(result)
        
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

        string = self.Lookup("DEF", strData)
        if string:
            pNode.setDEF(string)
            CX3DScene.m_Node.append(pNode)

        string = self.Lookup("USE", strData)
        if string:
            pNode.setUSE(string)

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
            pNode.setRadius(result)

        string = self.Lookup("DEF", strData)
        if string:
            pNode.setDEF(string)

        string = self.Lookup("USE", strData)
        if string:
            pNode.setUSE(string)

        self.AddNode(pNode, flag)

    def ElementMaterial(self, strData, flag):
        pNode = CMaterial()

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

        string = self.Lookup("DEF", strData)
        if string:
            pNode.setDEF(string)
            CX3DScene.m_Node.append(pNode)

        string = self.Lookup("USE", strData)
        if string:
            pNode.setUSE(string)

        self.AddNode(pNode, flag)

    def ElementBackground(self, strData, flag):
        pNode = CBackground()

        string = self.Lookup("skyColor", strData)
        if string:
            cval = CSFColor()
            self.GetValue3(string, cval)
            pNode.setSkyColor3(cval)
        
        string = self.Lookup("DEF", strData)
        if string:
            pNode.setDEF(string)
            CX3DScene.m_Node.append(pNode)

        string = self.Lookup("USE", strData)
        if string:
            pNode.setUSE(string)

        self.AddNode(pNode, flag)

    def ElementScript(self, strData, flag):
        pNode = CScript()

        string = self.Lookup("url", strData)
        if string:
            pNode.setURL(string)

        string = self.Lookup("DEF", strData)
        if string:
            pNode.setDEF(string)
            CX3DScene.m_Node.append(pNode)

        string = self.Lookup("USE", strData)
        if string:
            pNode.setUSE(string)

        CX3DScene.m_Script = pNode

        self.AddNode(pNode, flag)
    
    def ElementField(self, strData, flag):
        pNode = CField()

        string = self.Lookup("accessType", strData)
        if string:
            pNode.setAccessType(string)

        string = self.Lookup("name", strData)
        if string:
            pNode.setName(string)

        string = self.Lookup("type", strData)
        if string:
            pNode.setType(string)

        string = self.Lookup("value", strData)
        if string:
            pNode.setValue(string)

        string = self.Lookup("appinfo", strData)
        if string:
            pNode.setAppInfo(string)

        string = self.Lookup("documentation", strData)
        if string:
            pNode.setDocumentation(string)

        string = self.Lookup("field", strData)
        if string:
            pNode.setField(string)

        string = self.Lookup("DEF", strData)
        if string:
            pNode.setDEF(string)

        string = self.Lookup("USE", strData)
        if string:
            pNode.setUSE(string)
            CX3DScene.m_Node.append(pNode)

        CX3DScene.m_fields.Add(pNode)

        self.AddNode(pNode, flag)
    
    def ElementROUTE(self, strData, flag):
        pNode = CROUTE()

        string = self.Lookup("DEF", strData)
        if string:
            pNode.setDEF(string)

        string = self.Lookup("toField", strData)
        if string:
            pNode.setToField(string)

        string = self.Lookup("fromField", strData)
        if string:
            pNode.setFromField(string)

        string = self.Lookup("fromNode", strData)
        if string:
            pNode.setFromNode(string)

        string = self.Lookup("toNode", strData)
        if string:
            pNode.setToNode(string)

        string = self.Lookup("SourceNode", strData)
        if string:
            pNode.setSourceNode(string)

        string = self.Lookup("DestinationNode", strData)
        if string:
            pNode.setDestinationNode(string)

        string = self.Lookup("DEF", strData)
        if string:
            pNode.setDEF(string)
            CX3DScene.m_Node.append(pNode)

        string = self.Lookup("USE", strData)
        if string:
            pNode.setUSE(string)

        CX3DScene.m_ROUTE.append(pNode)

        self.AddNode(pNode, flag)

    def ElementTransform(self, strData, flag):
        pNode = CTransform()

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
            pNode.setScaleOrientation2(Vec)

        string = self.Lookup("translation", strData)
        if string:
            Vec = CSFVec3f()
            self.GetValue3(string, Vec)
            pNode.setTranslation2(Vec)

        string = self.Lookup("DEF", strData)
        if string:
            pNode.setDEF(string)
            CX3DScene.m_Node.append(pNode)

        string = self.Lookup("USE", strData)
        if string:
            pNode.setUSE(string)

        self.AddNode(pNode, flag)
    
    def ElementGroup(self, strData, flag):
        pNode = CGroup()

        string = self.Lookup("DEF", strData)
        if string:
            pNode.setDEF(string)
            CX3DScene.m_Node.append(pNode)

        string = self.Lookup("USE", strData)
        if string:
            pNode.setUSE(string)

        self.AddNode(pNode, flag)

    def ElementBody(self, strData, flag):
        pNode = CBody()

        string = self.Lookup("DEF", strData)
        if string:
            pNode.setDEF(string)
            CX3DScene.m_Node.append(pNode)

        string = self.Lookup("USE", strData)
        if string:
            pNode.setUSE(string)

        self.AddNode(pNode, flag)

    def ElementScene(self, strData, flag):
        pNode = CScene()

        string = self.Lookup("DEF", strData)
        if string:
            pNode.setDEF(string)
            CX3DScene.m_Node.append(pNode)

        string = self.Lookup("USE", strData)
        if string:
            pNode.setUSE(string)

        CX3DScene.m_Scene = pNode

        self.AddNode(pNode, flag)

    def ElementTouchSensor(self, strData, flag):
        pNode = CTouchSensor()

        string = self.Lookup("DEF", strData)
        if string:
            pNode.setDEF(string)
            CX3DScene.m_Node.append(pNode)

        string = self.Lookup("USE", strData)
        if string:
            pNode.setUSE(string)

        CX3DScene.m_TouchSensor = pNode

        self.AddNode(pNode, flag)

    def ElementShape(self, strData, flag):
        pNode = CShape()

        string = self.Lookup("DEF", strData)
        if string:
            pNode.setDEF(string)
            CX3DScene.m_Node.append(pNode)

        string = self.Lookup("USE", strData)
        if string:
            pNode.setUSE(string)

        self.AddNode(pNode, flag)

    def ElementAppearance(self, strData, flag):
        pNode = CAppearance()

        string = self.Lookup("DEF", strData)
        if string:
            pNode.setDEF(string)
            CX3DScene.m_Node.append(pNode)

        string = self.Lookup("USE", strData)
        if string:
            pNode.setUSE(string)

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

    def ElementTextureCoordinate(self, strData, flag):
        pNode = CTextureCoordinate()

        string = self.Lookup("point", strData)
        if string:
            pNode.setPoint(strData)

        string = self.Lookup("DEF", strData)
        if string:
            pNode.setDEF(string)
            CX3DScene.m_Node.append(pNode)

        string = self.Lookup("USE", strData)
        if string:
            pNode.setUSE(string)
        
        self.AddNode(pNode, flag)

    def ElementCoordinate(self, strData, flag):
        pNode = CCoordinate()

        string = self.Lookup("point", strData)
        if string:
            pNode.setPoint(strData)

        string = self.Lookup("DEF", strData)
        if string:
            pNode.setDEF(string)
            CX3DScene.m_Node.append(pNode)

        string = self.Lookup("USE", strData)
        if string:
            pNode.setUSE(string)

        self.AddNode(pNode, flag)

    def ElementNormal(self, strData, flag):
        pass

    def ElementIndexedFaceSet(self, strData, flag):
        pNode = CIndexedFaceSet()

        string = self.Lookup("solid", strData)
        result = self.GetSolid(string)
        if result != True:
            pNode.setSolid(False)

        string = self.Lookup("ccw", strData)
        result = self.GetSolid(string)
        if result != True:
            pNode.setCCW(False)

        string = self.Lookup("coordIndex", strData)
        if string:
            pNode.setCoordIndex(strData)

        string = self.Lookup("texCoordIndex", strData)
        if string:
            pNode.setTexCoordIndex(strData)

        string = self.Lookup("creaseAngle", strData)
        if string:
            result = float(string)
            pNode.setcreaseAngle(result)

        string = self.Lookup("DEF", strData)
        if string:
            pNode.setDEF(string)
            CX3DScene.m_Node.append(pNode)

        string = self.Lookup("USE", strData)
        if string:
            pNode.setUSE(string)

        self.AddNode(pNode, flag)
        
    def ElementImageTexture(self, strData, flag):
        pNode = CImageTexture()
        
        string = self.Lookup("url", strData)
        if string:
            pNode.setURL(
                string, self.filepath, 
                CX3DScene.m_TextureNode
            )

        string = self.Lookup("DEF", strData)
        if string:
            pNode.setDEF(string)
            CX3DScene.m_Node.append(pNode)

        string = self.Lookup("USE", strData)
        if string:
            pNode.setUSE(string)

        self.AddNode(pNode, flag)

    def ElementNode(self, strData, flag):
        pNode = CX3DNode()
        self.AddNode(pNode, flag)

    def X3D_parse(self, filepath):
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
            strData = strData.replace('"', "'")
            strData = strData.replace(',', '')
            strData = strData.replace(" '/>", "'/>")
            strData = strData.replace("' ", "'")
            strData = strData.replace("''", "'")
            if not strData:
                break

            # </
            nDelimiter = strData.find(strValue1)
            if nDelimiter > 0 :
                CX3DTree.m_Node = CX3DTree.m_Node.m_Parent[0]
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

    def WRL_parse(self, filepath):
        pass

if __name__=="__main__":
    m_pScene = CX3DScene()