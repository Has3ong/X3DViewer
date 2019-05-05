from . import *

class CCollisionSpace(CX3DNBodyCollisionSpaceNode):
    m_strNodeName = "CollisionSpace"
    def __init__(self):
        self.m_strNodeName = "CollisionSpace"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass