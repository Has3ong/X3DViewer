from . import *

class CGeoCoordinate(CX3DCoordinateNode):
    m_strNodeName = "GeoCoordinate"
    def __init__(self):
        self.m_strNodeName = "GeoCoordinate"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass