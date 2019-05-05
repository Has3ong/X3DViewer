from . import *

class CNurbsSurfaceInterpolator(CX3DChildNode):
    m_strNodeName = "NurbsSurfaceInterpolator"
    def __init__(self):
        self.m_strNodeName = "NurbsSurfaceInterpolator"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass