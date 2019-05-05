from . import *

class CStaticGroup(CX3DChildNode):
    m_strNodeName = "StaticGroup"
    def __init__(self):
        self.m_strNodeName = "StaticGroup"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass