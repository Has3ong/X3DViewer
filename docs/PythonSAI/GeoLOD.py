from . import *

class CGeoLOD(CX3DChildNode):
    m_strNodeName = "GeoLOD"
    def __init__(self):
        self.m_strNodeName = "GeoLOD"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass