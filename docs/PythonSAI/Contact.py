from . import *

class CContact(CX3DNode):
    m_strNodeName = "Contact"
    def __init__(self):
        self.m_strNodeName = "Contact"
        self.m_Parent = [None]
        self.children = []
        self.SourceNode = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
 

    pass