from . import *

class CInline(CX3DChildNode):
    m_strNodeName = "Inline"
    def __init__(self):
        self.m_strNodeName = "Inline"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass