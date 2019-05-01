from . import *

class CX3DPickableObject(CX3DRootNode):
    m_strNodeName = "X3DPickableObject"
    def __init__(self):
        self.m_strNodeName = "X3DPickableObject"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
 
    pass