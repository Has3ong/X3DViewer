from . import *

class CAudioClip(CX3DSoundSourceNode):
    m_strNodeName = "AudioClip"
    def __init__(self):
        self.m_strNodeName = "AudioClip"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass