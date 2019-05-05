from . import *

class CTextureBackground(CX3DBackgroundNode):
    m_strNodeName = "TextureBackground"
    def __init__(self):
        self.m_strNodeName = "TextureBackground"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass