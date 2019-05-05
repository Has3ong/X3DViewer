from . import *

class CBillboard(CX3DGroupingNode):
    m_strNodeName = "Billboard"
    def __init__(self):
        self.m_strNodeName = "Billboard"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass