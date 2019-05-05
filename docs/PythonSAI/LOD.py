from . import *

class CLOD(CX3DGroupingNode):
    m_strNodeName = "LOD"
    def __init__(self):
        self.m_strNodeName = "LOD"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass