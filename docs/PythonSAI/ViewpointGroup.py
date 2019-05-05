from . import *

class CViewpointGroup(CX3DViewpointNode):
    m_strNodeName = "ViewpointGroup"
    def __init__(self):
        self.m_strNodeName = "ViewpointGroup"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass