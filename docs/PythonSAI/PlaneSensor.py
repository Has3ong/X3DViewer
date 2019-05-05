from . import *

class CPlaneSensor(CX3DDragSensorNode):
    m_strNodeName = "PlaneSensor"
    def __init__(self):
        self.m_strNodeName = "PlaneSensor"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass