from . import *

class COrthoViewpoint(CX3DViewpointNode):
    m_strNodeName = "OrthoViewpoint"
    def __init__(self):
        self.m_strNodeName = "OrthoViewpoint"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass