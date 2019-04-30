from . import *

class CX3DSensorNode(CX3DChildNode):

    m_strNodeName = "CX3DSensorNode"
    DEF = ""

    enabled = True
    isActive = True

    def __init__(self):
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""

    def setIsActive(self, value):
        self.isActive = value

    def getIsActive(self):
        return self.isActive

    def setEnabled(self, value):
        self.enabled = value

    def getEnabled(self):
        return self.enabled

    def setDEF(self, value):
        self.DEF = value

    def getDEF(self):
        return self.DEF

    