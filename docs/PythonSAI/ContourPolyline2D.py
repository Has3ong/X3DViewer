from . import *

class CContourPolyline2D(CX3DNurbsControlCurveNode):
    m_strNodeName = "ContourPolyline2D"
    def __init__(self):
        self.m_strNodeName = "ContourPolyline2D"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass