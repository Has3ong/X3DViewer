from . import *

class CTextureCoordinateGenerator(CX3DTextureCoordinateNode):
    m_strNodeName = "TextureCoordinateGenerator"
    def __init__(self):
        self.m_strNodeName = "TextureCoordinateGenerator"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass