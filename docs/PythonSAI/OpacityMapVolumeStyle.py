from . import *

class COpacityMapVolumeStyle(CX3DComposableVolumeRenderStyle):
    m_strNodeName = "OpacityMapVolumeStyle"
    def __init__(self):
        self.m_strNodeName = "OpacityMapVolumeStyle"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass