from . import *

class CBackground(CX3DBackgroundNode):
    m_strNodeName = "Background"
    def __init__(self):
        self.m_Parent = [None]
        self.children = []

        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
 
    pass