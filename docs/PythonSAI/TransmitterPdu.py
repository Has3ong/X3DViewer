from . import *

class CTransmitterPdu(CX3DSensorNode):
    m_strNodeName = "TransmitterPdu"
    def __init__(self):
        self.m_strNodeName = "TransmitterPdu"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass