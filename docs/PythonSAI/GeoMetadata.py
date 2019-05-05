from . import *

class CGeoMetadata(CX3DInfoNode):
    m_strNodeName = "GeoMetadata"
    def __init__(self):
        self.m_strNodeName = "GeoMetadata"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass