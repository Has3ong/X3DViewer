from . import *

class CNormal(CX3DNormalNode):
    m_strNodeName = "Normal"
    def __init__(self):
        self.m_strNodeName = "Normal"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass