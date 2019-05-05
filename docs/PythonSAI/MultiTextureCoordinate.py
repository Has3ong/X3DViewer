from . import *

class CMultiTextureCoordinate(CX3DTextureCoordinateNode):
    m_strNodeName = "MultiTextureCoordinate"
    def __init__(self):
        self.m_strNodeName = "MultiTextureCoordinate"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass