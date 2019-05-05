from . import *

class CX3DDamperNode(CX3DFollowerNode):
    m_strNodeName = "X3DDamperNode"
    def __init__(self):
        self.m_strNodeName = "X3DDamperNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass