from . import *

class CQuadSet(CX3DComposedGeometryNode):
    m_strNodeName = "QuadSet"
    def __init__(self):
        self.m_strNodeName = "QuadSet"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

    pass