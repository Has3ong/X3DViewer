from . import *

class CX3DChildNode(CX3DNode):
    m_strNodeName = "X3DChildNode"
    def __init__(self):
        self.m_strNodeName = "X3DChildNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

    pass