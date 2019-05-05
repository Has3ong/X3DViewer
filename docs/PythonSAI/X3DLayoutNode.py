from . import *

class CX3DLayoutNode(CX3DChildNode):
    m_strNodeName = "X3DLayoutNode"
    def __init__(self):
        self.m_strNodeName = "X3DLayoutNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass