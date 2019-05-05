from . import *

class CMatrix4VertexAttribute(CX3DVertexAttributeNode):
    m_strNodeName = "Matrix4VertexAttribute"
    def __init__(self):
        self.m_strNodeName = "Matrix4VertexAttribute"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass