from . import *

class CIntegerTrigger(CX3DTriggerNode):
    m_strNodeName = "IntegerTrigger"
    def __init__(self):
        self.m_strNodeName = "IntegerTrigger"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass