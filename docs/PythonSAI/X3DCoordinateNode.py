from . import *

class CX3DCoordinateNode(CX3DGeometricPropertyNode):
    m_strNodeName = "X3DCoordinateNode"
    def __init__(self):
        self.m_strNodeName = "X3DCoordinateNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass