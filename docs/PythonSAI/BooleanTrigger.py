from . import *

class CBooleanTrigger(CX3DTriggerNode):
    m_strNodeName = "BooleanTrigger"
    def __init__(self):
        self.m_strNodeName = "BooleanTrigger"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass