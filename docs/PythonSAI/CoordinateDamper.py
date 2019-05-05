from . import *

class CCoordinateDamper(CX3DDamperNode):
    m_strNodeName = "CoordinateDamper"
    def __init__(self):
        self.m_strNodeName = "CoordinateDamper"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass