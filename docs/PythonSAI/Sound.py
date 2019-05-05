from . import *

class CSound(CX3DSoundNode):
    m_strNodeName = "Sound"
    def __init__(self):
        self.m_strNodeName = "Sound"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass