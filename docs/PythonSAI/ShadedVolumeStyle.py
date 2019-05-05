from . import *

class CShadedVolumeStyle(CX3DComposableVolumeRenderStyle):
    m_strNodeName = "ShadedVolumeStyle"
    def __init__(self):
        self.m_strNodeName = "ShadedVolumeStyle"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass