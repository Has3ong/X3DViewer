from . import *

class CText(CX3DGeometryNode):
    m_strNodeName = "Text"
    def __init__(self):
        self.m_strNodeName = "Text"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

    pass