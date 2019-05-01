from . import *

class CX3DRootNode():
    DEF = ""
    USE = ""
    m_strNodeName = "X3DRootNode"
    m_Parent = [None]
    children = []
    n_Count = -1
    depth = 0
    def __init__(self):
        self.m_strNodeName = "X3DRootNode"
        self.DEF = ""
        self.USE = ""
        self.m_Parent = [None]
        self.children = []
        self.n_Count = -1
        self.depth = 0

    def init(self):
        self.DEF = ""
        self.USE = ""
        self.m_Parent = [None]
        self.children = []
        self.n_Count = -1
        self.depth = 0
        
    def setID(self, id):
        self.nID = id

    def getID(self):
        return self.nID
    
    def setNodeName(self, strName):
        self.m_strNodeName = strName

    def getNodeName(self):
        return self.m_strNodeName

    def isNodeName(self, strName):
        bRet = False
        if self.m_strNodeName == strName:
            bRet = True

        return bRet

    def addChildren(self, pNode):
        pNode.m_Parent[0] = self
        self.children.append(pNode)
        self.n_Count += 1
    
    def insertChildren(self, child):
        child.m_Parent[0] = self
        children.insert(0, child)

    def removeChildren(self, child):
        nSize = len(children)

        for i in range(0, nSize):
            temp = CX3DRootNode()
            temp = children[i]
            if temp == child:
                del self.children[i]

    def addRootNode(self, pNode):
        pNode.m_Parent[0]
        self.children.append(pNode)
        self.n_Count += 1

    def getSource(self):
        return self.m_tofield[0]

    def getDEF(self):
        return self.DEF

    def setDEF(self, strDef):
        self.DEF = strDef
    
    def setUSE(self, strDef):
        self.USE = strDef

    def getUSE(self):
        return self.USE


