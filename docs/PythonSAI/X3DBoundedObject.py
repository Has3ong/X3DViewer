from . import *

class CX3DBoundedObject(CX3DRootNode):
    m_strNodeName = "X3DBoundedObject"
    def __init__(self):
        self.m_strNodeName = "X3DBoundedObject"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

    pass