from . import *

class CMeta(CX3DNode):
    m_strNodeName = "Meta"
    content = ""
    name = ""
    def __init__(self):
        self.m_strNodeName = "Meta"
        self.m_Parent = [None]
        self.children = []
        self.SourceNode = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

    def setContent(self, value):
        self.content = value

    def setName(self, value):
        self.name = value