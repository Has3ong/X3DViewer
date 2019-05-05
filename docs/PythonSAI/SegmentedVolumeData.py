from . import *

class CSegmentedVolumeData(CX3DVolumeDataNode):
    m_strNodeName = "SegmentedVolumeData"
    def __init__(self):
        self.m_strNodeName = "SegmentedVolumeData"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass