from . import *

class CLayoutGroup(CX3DGroupingNode):
    m_strNodeName = "LayoutGroup"
    def __init__(self):
        self.m_strNodeName = "LayoutGroup"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass