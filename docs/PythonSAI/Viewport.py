from . import *

class CViewport(CX3DViewportNode):
    m_strNodeName = "Viewport"
    def __init__(self):
        self.m_strNodeName = "Viewport"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass