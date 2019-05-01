from . import *

class CTextureTransfrom(CX3DTextureTransformNode):
    m_strNodeName = "TextureTransform"
    def __init__(self):
        self.m_strNodeName = "TextureTransform"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
 
    pass