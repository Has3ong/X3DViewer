from . import *

class CROUTE(CSceneGraphStructureStatement):
    m_strNodeName = "ROUTE"
    DEF = ""

    fromField = ""
    fromNode = ""
    toField = ""
    toNode = ""

    m_pSourceNode = []
    m_pDestinationNode = []

    def __init__(self):
        self.m_strNodeName = "ROUTE"
        self.fromField = ""
        self.fromNode = ""
        self.toField = ""
        self.toNode = ""
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1


        self.m_fromNode = []
        self.m_toNode = []

        self.m_Parent = [None]
        self.children = []
        
    def setDEF(self, value):
        self.DEF = value

    def getDEF(self):
        return self.DEF

    def setFromField(self, value):
        self.fromField = value

    def getFromField(self):
        return self.fromField

    def setFromNode(self, value):
        self.fromNode = value

    def getFromNode(self):
        return self.fromNode

    def setToField(self, value):
        self.toField = value

    def getToField(self):
        return self.toField

    def setToNode(self, value):
        self.toNode = value

    def getToNode(self):
        return self.toNode

    def setSourceNode(self, value):
        self.m_pSourceNode[0] = value

    def getSourceNode(self):
        return self.m_pSourceNode[0]

    def setDestinationNode(self, value):
        self.m_pDestinationNode[0] = value

    def getDestinationNode(self):
        return self.m_pDestinationNode[0]


    