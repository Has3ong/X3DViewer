from . import *

class CX3DNode(CX3DRootNode):
    m_strNodeName = "X3DNode"
    metadata = ""
    DEF = ""
    USE = ""
    SourceNode = []
    depth = 0

    def __init__(self):
        self.m_strNodeName = "X3DNode"
        self.metadata = ""
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

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
