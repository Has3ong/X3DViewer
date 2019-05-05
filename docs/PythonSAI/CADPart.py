from . import *
#CX3DProductStructureChildNode
class CCADPart(CX3DGroupingNode):
    m_strNodeName = "CADPart"
    def __init__(self):
        self.m_strNodeName = "CADPart"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass