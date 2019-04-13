from X3DLib import *

class CX3DNode(CX3DRootNode):
    m_strNodeName = "X3DNode"
    metadata = ""
    DEF = ""
    USE = ""
    SourceNode = []

    #def Draw(self):
    #def toXMLString(self):
    #def getPropertyString(self):

    def __init__(self):
        self.m_Parent = [None]
        self.children = []
        self.SourceNode = []
        self.DEF = ""
        self.USE = ""

    def getMetadata(self):
        return self.metadata

    def setMetadata1(self, node):
        self.metadata = node

    def setMetadata2(self, protoInstance):
        self.metadata = protoInstance

    def getDEF(self):
        return self.DEF

    def setDEF(self, strDef):
        self.DEF = strDef
        
    def disposs(self):
        return None

    def getField(self, name):
        return None

    def getFieldDefinitions(self):
        return None
    
    def getNodeName(self):
        return ""

    def isRealized(self):
        return True

    def realize(self):
        return None

    def setUSE(self, value):
        self.USE = value

    def getUSE(self):
        return self.USE