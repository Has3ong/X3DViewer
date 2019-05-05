from . import *

class CTimeTrigger(CX3DTriggerNode):
    m_strNodeName = "TimeTrigger"
    def __init__(self):
        self.m_strNodeName = "TimeTrigger"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass