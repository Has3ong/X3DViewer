from . import *

class CHAnimJoint(CX3DGroupingNode):
    m_strNodeName = "HAnimJoint"
    def __init__(self):
        self.m_strNodeName = "HAnimJoint"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass