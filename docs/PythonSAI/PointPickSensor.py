from . import *

class CPointPickSensor(CX3DPickSensorNode):
    m_strNodeName = "PointPickSensor"
    def __init__(self):
        self.m_strNodeName = "PointPickSensor"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass