from . import *

class CX3DBindableNode(CX3DChildNode):
    m_strNodeName = "X3DBindanbleNode"
    bound = True
    bindTime = 0.0
    def __init__(self):
        self.m_strNodeName = "X3DBindableNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

        self.bound = True
        self.bindTime = 0.0
    def setBind(self, value):
        self.bound = value

    def getBindTime(self):
        return self.bindTime

    def getIsBound(self):
        return self.bound