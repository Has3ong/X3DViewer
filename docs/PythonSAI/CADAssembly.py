from . import *
#CX3DProductStructureChildNode
class CCADAssembly(CX3DGroupingNode):
    m_strNodeName = "CADAssembly"
    def __init__(self):
        self.m_strNodeName = "CADAssembly"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass