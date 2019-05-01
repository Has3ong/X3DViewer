from . import *

class CMultiTextureTransform(CX3DTextureTransformNode):
    m_strNodeName = "MultiTextureTransform"
    def __init__(self):
        self.m_strNodeName = "MultiTextureTransform"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

    pass