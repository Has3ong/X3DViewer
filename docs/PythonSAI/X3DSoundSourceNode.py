from . import *

class CX3DSoundSourceNode(CX3DTimeDependentNode):
    m_strNodeName = "X3DSoundSourceNode"
    def __init__(self):
        self.m_strNodeName = "X3DSoundSourceNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass