from . import *

class CClipPlane(CX3DChildNode):
    m_strNodeName = "ClipPlane"
    def __init__(self):
        self.m_strNodeName = "ClipPlane"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass