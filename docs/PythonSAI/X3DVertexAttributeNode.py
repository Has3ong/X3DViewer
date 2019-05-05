from . import *

class CX3DVertexAttributeNode(CX3DGeometricPropertyNode):
    m_strNodeName = "X3DVertexAttributeNode"
    def __init__(self):
        self.m_strNodeName = "X3DVertexAttributeNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass