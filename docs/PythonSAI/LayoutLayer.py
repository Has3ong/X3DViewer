from . import *

class CLayoutLayer(CX3DLayerNode):
    m_strNodeName = "LayoutLayer"
    def __init__(self):
        self.m_strNodeName = "LayoutLayer"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass