from . import *
#CX3DSensorNode
class CCollision(CX3DGroupingNode):
    m_strNodeName = "Collision"
    def __init__(self):
        self.m_strNodeName = "Collision"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass