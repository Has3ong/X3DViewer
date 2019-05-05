from . import *

class CStringSensor(CX3DKeyDeviceSensorNode):
    m_strNodeName = "StringSensor"
    def __init__(self):
        self.m_strNodeName = "StringSensor"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass