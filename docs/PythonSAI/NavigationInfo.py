from . import *

class CNavigationInfo(CX3DBindableNode):
    m_strNodeName = "NavigationInfo"
    def __init__(self):
        self.m_strNodeName = "NavigationInfo"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass