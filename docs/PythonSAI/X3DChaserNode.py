from . import *

class CX3DChaserNode(CX3DFollowerNode):
    m_strNodeName = "X3DChaserNode"
    def __init__(self):
        self.m_strNodeName = "X3DChaserNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass