from . import *

class CCADFace(CX3DProductStructureChildNode):
    m_strNodeName = "CADFace"
    def __init__(self):
        self.m_strNodeName = "CADFace"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass