from . import *

class CTextureCoordinate(CX3DTextureCoordinateNode):
    m_strNodeName = "TextureCoordinate"

    def __init__(self):
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.point = []

    def setAttribute(self, Node):
        self.point = Node.point