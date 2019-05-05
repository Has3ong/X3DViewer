from . import *

class CLayer(CX3DLayerNode):
    m_strNodeName = "Layer"
    def __init__(self):
        self.m_strNodeName = "Layer"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass