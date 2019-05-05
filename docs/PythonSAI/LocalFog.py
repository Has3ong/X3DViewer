from . import *

class CLocalFog(CX3DChildNode):
    m_strNodeName = "LocalFog"
    def __init__(self):
        self.m_strNodeName = "LocalFog"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass