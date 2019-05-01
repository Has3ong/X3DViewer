from . import *

class CX3DMetadataObject(CX3DRootNode):
    m_strNodeName = "X3DMetadataObject"
    def __init__(self):
        self.m_strNodeName = "X3DMetadataObject"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass