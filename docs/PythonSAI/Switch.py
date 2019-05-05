from . import *

class CSwitch(CX3DGroupingNode):
    m_strNodeName = "Switch"
    def __init__(self):
        self.m_strNodeName = "Switch"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass