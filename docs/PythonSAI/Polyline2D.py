from . import *

class CPolyline2D(CX3DGeometryNode):
    m_strNodeName = "Polyline2D"
    def __init__(self):
        self.m_strNodeName = "Polyline2D"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

    pass