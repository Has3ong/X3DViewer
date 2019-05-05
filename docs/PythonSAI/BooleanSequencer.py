from . import *

class CBooleanSequencer(CX3DSequencerNode):
    m_strNodeName = "BooleanSequencer"
    def __init__(self):
        self.m_strNodeName = "BooleanSequencer"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass