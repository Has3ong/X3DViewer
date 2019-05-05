from . import *

class CWorldInfo(CX3DInfoNode):
    m_strNodeName = "WorldInfo"
    def __init__(self):
        self.m_strNodeName = "WorldInfo"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass