from . import *

class CIsoSurfaceVolumeData(CX3DVolumeDataNode):
    m_strNodeName = "IsoSurfaceVolumeData"
    def __init__(self):
        self.m_strNodeName = "IsoSurfaceVolumeData"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass