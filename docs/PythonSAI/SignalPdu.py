from . import *

class CSignalPdu(CX3DSensorNode):
    m_strNodeName = "SignalPdu"
    def __init__(self):
        self.m_strNodeName = "SignalPdu"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass