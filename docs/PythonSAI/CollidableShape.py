from . import *

class CCollidableShape(CX3DNBodyCollidableNode):
    m_strNodeName = "CollidableShape"
    def __init__(self):
        self.m_strNodeName = "CollidableShape"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass