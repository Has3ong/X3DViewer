from . import *

class CNurbsTrimmedSurface(CX3DNurbsSurfaceGeometryNode):
    m_strNodeName = "NurbsTrimmedSurface"
    def __init__(self):
        self.m_strNodeName = "NurbsTrimmedSurface"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

    pass