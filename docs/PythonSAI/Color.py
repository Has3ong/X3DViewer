from . import *

class CColor(CX3DColorNode):
    m_strNodeName = "Color"
    def __init__(self):
        self.m_strNodeName = "Color"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass