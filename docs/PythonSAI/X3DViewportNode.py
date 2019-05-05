from . import *

class CX3DViewportNode(CX3DGroupingNode):
    m_strNodeName = "X3DViewportNode"
    def __init__(self):
        self.m_strNodeName = "X3DViewportNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass