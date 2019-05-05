from . import *

class CX3DTimeDependentNode(CX3DChildNode):
    m_strNodeName = "X3DTimeDependentNode"
    def __init__(self):
        self.m_strNodeName = "X3DTimeDependentNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass