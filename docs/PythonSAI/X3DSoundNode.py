from . import *

class CX3DSoundNode(CX3DChildNode):
    m_strNodeName = "X3DSoundNode"
    def __init__(self):
        self.m_strNodeName = "X3DSoundNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass