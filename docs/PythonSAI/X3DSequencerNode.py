from . import *

class CX3DSequencerNode(CX3DChildNode):
    m_strNodeName = "X3DSequencerNode"
    def __init__(self):
        self.m_strNodeName = "X3DSequencerNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass