from . import *

class CPositionChaser(CX3DChaserNode):
    m_strNodeName = "PositionChaser"
    def __init__(self):
        self.m_strNodeName = "PositionChaser"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass