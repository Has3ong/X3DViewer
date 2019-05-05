from . import *

class CGeoTransform(CX3DGroupingNode):
    m_strNodeName = "GeoTransform"
    def __init__(self):
        self.m_strNodeName = "GeoTransform"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass