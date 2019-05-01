from . import *

class CIndexedTriangleSet(CX3DGeometryNode):
    m_strNodeName = "IndexedTriangleSet"
    def __init__(self):
        self.m_strNodeName = "IndexedTriangleSet"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
 
    pass