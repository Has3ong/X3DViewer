from . import *

class CTriangleSet(CX3DComposedGeometryNode):
    m_strNodeName = "TriangleSet"
    def __init__(self):
        self.m_strNodeName = "TriangleSet"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

    pass