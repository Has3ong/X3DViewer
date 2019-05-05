from . import *

class CX3DNormalNode(CX3DGeometricPropertyNode):
    m_strNodeName = "X3DNormalNode"
    def __init__(self):
        self.m_strNodeName = "X3DNormalNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass