from . import *

class CX3DMaterialNode(CX3DAppearanceChildNode):
    m_strNodeName = "X3DMaterialNode"
    def __init__(self):
        self.m_strNodeName = "X3DMaterialNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass