from . import *

class CVolumePickSensor(CX3DPickSensorNode):
    m_strNodeName = "VolumePickSensor"
    def __init__(self):
        self.m_strNodeName = "VoluePickSensor"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass