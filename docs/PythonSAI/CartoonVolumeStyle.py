from . import *

class CCartoonVolumeStyle(CX3DComposableVolumeRenderStyle):
    m_strNodeName = "CartoonVolumeStyle"
    def __init__(self):
        self.m_strNodeName = "CartoonVolumeStyle"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass