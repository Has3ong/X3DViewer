from . import *

class CHAnimSegment(CX3DGroupingNode):
    m_strNodeName = "HAnimSegment"
    def __init__(self):
        self.m_strNodeName = "HAnimSegment"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass