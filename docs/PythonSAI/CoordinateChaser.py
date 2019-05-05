from . import *

class CCoordinateChaser(CX3DChaserNode):
    m_strNodeName = "CoordinateChaser"
    def __init__(self):
        self.m_strNodeName = "CoordinateChaser"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass