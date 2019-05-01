from . import *

class CX3DScriptNode(CX3DUrlObject):
    m_strNodeName = "X3DScriptNode"
    def __init__(self):
        self.m_strNodeName = "X3DScriptNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

    pass