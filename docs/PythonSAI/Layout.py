from . import *

class CLayout(CX3DLayoutNode):
    m_strNodeName = "Layout"
    def __init__(self):
        self.m_strNodeName = "Layout"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass