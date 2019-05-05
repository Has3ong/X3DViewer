from . import *

class CVolumeData(CX3DVolumeDataNode):
    m_strNodeName = "VolumeData"
    def __init__(self):
        self.m_strNodeName = "VolumeData"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass