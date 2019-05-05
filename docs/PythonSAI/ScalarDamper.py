from . import *

class CScalarDamper(CX3DDamperNode):
    m_strNodeName = "ScalarDamper"
    def __init__(self):
        self.m_strNodeName = "ScalarDamper"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass