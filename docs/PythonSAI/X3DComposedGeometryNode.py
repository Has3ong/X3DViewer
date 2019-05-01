from . import *

class CX3DComposedGeometryNode(CX3DGeometryNode):
    m_strNodeName = "X3DComposedGeometryNode"
    def __init__(self):
        self.m_strNodeName = "X3DComposedGeometryNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass