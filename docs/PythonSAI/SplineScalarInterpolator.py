from . import *

class CSplineScalarInterpolator(CX3DInterpolatorNode):
    m_strNodeName = "SplineScalarInterpolator"
    def __init__(self):
        self.m_strNodeName = "SplineScalarInterpolator"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass