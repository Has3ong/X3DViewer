from . import *

class CIntegerSequencer(CX3DSequencerNode):
    m_strNodeName = "IntegerSequencer"
    def __init__(self):
        self.m_strNodeName = "IntegerSequencer"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass