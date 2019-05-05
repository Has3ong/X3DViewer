from . import *

class CPositionInterpolator(CX3DInterpolatorNode):
    m_strNodeName = "PositionInterpolator"
    def __init__(self):
        self.m_strNodeName = "PositionInterpolator"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass