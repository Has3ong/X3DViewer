from . import *

class CCollisionCollection(CX3DChildNode):
    m_strNodeName = "CollisionCollection"
    def __init__(self):
        self.m_strNodeName = "CollisionCollection"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass