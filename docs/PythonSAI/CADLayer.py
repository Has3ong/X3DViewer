from . import *

class CCADLayer(CX3DGroupingNode):
    m_strNodeName = "CADLayer"
    def __init__(self):
        self.m_strNodeName = "CADLayer"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass