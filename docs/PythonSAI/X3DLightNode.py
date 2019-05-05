from . import *

class CX3DLightNode(CX3DChildNode):
    m_strNodeName = "X3DLightNode"
    def __init__(self):
        self.m_strNodeName = "X3DLightNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass