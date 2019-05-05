from . import *

class CScalarInterpolator(CX3DInterpolatorNode):
    m_strNodeName = "ScalarInterpolator"
    def __init__(self):
        self.m_strNodeName = "ScalarInterpolator"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass