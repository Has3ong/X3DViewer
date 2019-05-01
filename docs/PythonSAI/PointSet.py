from . import *

class CPointSet(CX3DGeometryNode):
    m_strNodeName = "PointSet"
    def __init__(self):
        self.m_strNodeName = "PointSet"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

    pass