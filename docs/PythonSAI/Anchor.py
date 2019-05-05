from . import *

class CAnchor(CX3DGroupingNode):
    m_strNodeName = "Anchor"
    def __init__(self):
        self.m_strNodeName = "Anchor"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass