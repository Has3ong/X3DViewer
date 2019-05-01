from . import *

class CTriangleFanSet(CX3DComposedGeometryNode):
    m_strNodeName = "TriangleFanSet"
    def __init__(self):
        self.m_strNodeName = "TriangleFanSet"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

    pass