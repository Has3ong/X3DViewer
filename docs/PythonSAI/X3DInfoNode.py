from . import *

class CX3DInfoNode(CX3DChildNode):
    m_strNodeName = "X3DInfoNode"
    def __init__(self):
        self.m_strNodeName = "X3DInfoNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass