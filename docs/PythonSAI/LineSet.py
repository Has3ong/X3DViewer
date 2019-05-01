from . import *

class CLineSet(CX3DGeometryNode):
    m_strNodeName = "LineSet"
    def __init__(self):
        self.m_strNodeName = "LineSet"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
 
    pass