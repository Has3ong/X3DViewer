from . import *

class CScreenGroup(CX3DGroupingNode):
    m_strNodeName = "ScreenGroup"
    def __init__(self):
        self.m_strNodeName = "ScreenGroup"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass