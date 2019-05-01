from . import *

class CTriangleStripSet(CX3DComposedGeometryNode):
    m_strNodeName = "TriangleStripSet"
    def __init__(self):
        self.m_strNodeName = "TriangleStripSet"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

    pass