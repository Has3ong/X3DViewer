from . import *

class CLayerSet(CX3DNode):
    m_strNodeName = "LayerSet"
    def __init__(self):
        self.m_strNodeName = "LayerSet"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
 

    pass