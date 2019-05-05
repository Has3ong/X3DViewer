from . import *

class CX3DVolumeDataNode(CX3DChildNode):
    m_strNodeName = "X3DVolumeDataNode"
    def __init__(self):
        self.m_strNodeName = "X3DVolumeDataNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass