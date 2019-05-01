from . import *

class CExtrusion(CX3DGeometryNode):
    m_strNodeName = "Extrusion"
    def __init__(self):
        self.m_strNodeName = "Extrusion"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
 
    pass