from . import *

class CPositionDamper(CX3DDamperNode):
    m_strNodeName = "PositionDamper"
    def __init__(self):
        self.m_strNodeName = "PositionDamper"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass