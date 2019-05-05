from . import *

class CColorInterpolator(CX3DInterpolatorNode):
    m_strNodeName = "ColorInterpolator"
    def __init__(self):
        self.m_strNodeName = "ColorInterpolator"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass