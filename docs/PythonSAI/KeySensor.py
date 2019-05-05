from . import *

class CKeySensor(CX3DKeyDeviceSensorNode):
    m_strNodeName = "KeySensor"
    def __init__(self):
        self.m_strNodeName = "KeySensor"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass