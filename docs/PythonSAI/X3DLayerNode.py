from . import *

class CX3DLayerNode(CX3DNode):
    m_strNodeName = "X3DLayerNode"
    def __init__(self):
        self.m_strNodeName = "X3DLayerNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass