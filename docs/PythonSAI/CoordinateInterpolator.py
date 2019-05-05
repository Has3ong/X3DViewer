from . import *

class CCoordinateInterpolator(CX3DInterpolatorNode):
    m_strNodeName = "CoordinateInterpolator"
    def __init__(self):
        self.m_strNodeName = "CoordinateInterpolator"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass