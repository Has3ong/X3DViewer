from . import *

class CDISEntityManager(CX3DChildNode):
    m_strNodeName = "DISEntityManager"
    def __init__(self):
        self.m_strNodeName = "DISEntityManager"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass