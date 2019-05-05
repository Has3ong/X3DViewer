from . import *

class CNormalInterpolator(CX3DInterpolatorNode):
    m_strNodeName = "NormalInterpolator"
    def __init__(self):
        self.m_strNodeName = "NormalInterpolator"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass