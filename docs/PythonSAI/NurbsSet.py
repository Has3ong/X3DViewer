from . import *

class CNurbsSet(CX3DChildNode):
    m_strNodeName = "NurbsSet"
    def __init__(self):
        self.m_strNodeName = "NurbsSet"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass