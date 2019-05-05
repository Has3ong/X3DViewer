from . import *

class CDISEntityTypeMapping(CX3DInfoNode):
    m_strNodeName = "DISEntityTypeMapping"
    def __init__(self):
        self.m_strNodeName = "DISEntityTypeMapping"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass