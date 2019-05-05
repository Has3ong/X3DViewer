from . import *

class CX3DFollowerNode(CX3DChildNode):
    m_strNodeName = "X3DFollowerNode"
    def __init__(self):
        self.m_strNodeName = "X3DFollowerNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass