from . import *

class COrientationDamper(CX3DDamperNode):
    m_strNodeName = "OrientationDamper"
    def __init__(self):
        self.m_strNodeName = "OrientationDamper"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass