from . import *

class CPixelTexture(CX3DTexture2DNode):
    m_strNodeName = "CPix3lTexture"
    def __init__(self):
        self.m_strNodeName = "PixelTexture"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

    pass