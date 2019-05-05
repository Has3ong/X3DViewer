from . import *

class CReceiverPdu(CX3DSensorNode):
    m_strNodeName = "ReceiverPdu"
    def __init__(self):
        self.m_strNodeName = "ReceiverPdu"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass