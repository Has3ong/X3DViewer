from . import *

class CLoadSensor(CX3DNetworkSensorNode):
    m_strNodeName = "LoadSensor"
    def __init__(self):
        self.m_strNodeName = "LoadSensor"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass