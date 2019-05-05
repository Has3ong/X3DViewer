from . import *

class CPickableGroup(CX3DGroupingNode):
    m_strNodeName = "PickableGroup"
    def __init__(self):
        self.m_strNodeName = "PickableGroup"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass