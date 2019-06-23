from . import *

class CX3DGeometryNode(CX3DNode):
    m_strNodeName = "X3DGeometryNode"
    def __init__(self):
        self.m_strNodeName = "X3DGeometryNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0
