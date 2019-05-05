from . import *
#CX3DTimeDependentNode
class CTimeSensor(CX3DTimeDependentNode):
    m_strNodeName = "TimeSensor"
    def __init__(self):
        self.m_strNodeName = "TimeSensor"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass