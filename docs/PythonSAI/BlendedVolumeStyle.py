from . import *

class CBlendedVolumeStyle(CX3DComposableVolumeRenderStyle):
    m_strNodeName = "BlendedVolumeStyle"
    def __init__(self):
        self.m_strNodeName = "BlendedVolumeStyle"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass