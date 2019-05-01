from . import *

class CNurbsCurve(CX3DParametricGeometryNode):
    m_strNodeName = "NurbsCurve"
    def __init__(self):
        self.m_strNodeName = "NurbsCurve"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

    pass