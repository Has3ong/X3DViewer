from . import *

class CFog(CX3DBindableNode):
    m_strNodeName = "Fog"
    def __init__(self):
        self.m_strNodeName = "Fog"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass