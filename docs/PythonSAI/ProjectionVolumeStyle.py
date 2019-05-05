from . import *

class CProjectionVolumeStyle(CX3DComposableVolumeRenderStyle):
    m_strNodeName = "ProjectionVolumeStyle"
    def __init__(self):
        self.m_strNodeName = "ProjectionVolumeStyle"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass