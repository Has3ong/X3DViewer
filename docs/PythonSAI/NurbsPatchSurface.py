from . import *

class CNurbsPatchSurface(CX3DNurbsSurfaceGeometryNode):
    m_strNodeName = "NurbsPatchSurface"
    def __init__(self):
        self.m_strNodeName = "NurbsPatchSurface"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

    pass