from . import *

class CCollidableOffset(CX3DNBodyCollidableNode):
    m_strNodeName = "CollidableOffset"
    def __init__(self):
        self.m_strNodeName = "CollidableOffset"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass