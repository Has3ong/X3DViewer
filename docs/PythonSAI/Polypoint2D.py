from . import *

class CPolyPoint2D(CX3DGeometryNode):
    m_strNodeName = "Polypoint2D"
    def __init__(self):
        self.m_strNodeName = "Polypoint2D"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

    pass