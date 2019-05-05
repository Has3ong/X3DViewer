from . import *

class CComposedVolumeStyle(CX3DComposableVolumeRenderStyle):
    m_strNodeName = "ComposedVolumeStyle"
    def __init__(self):
        self.m_strNodeName = "ComposedVolumeStyle"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass