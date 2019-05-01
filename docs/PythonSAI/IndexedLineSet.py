from . import *

class CIndexedLineSet(CX3DGeometryNode):
    m_strNodeName = "IndexedLineSet"
    def __init__(self):
        self.m_strNodeName = "IndexedLineSet"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
 
    pass