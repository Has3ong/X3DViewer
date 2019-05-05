from . import *

class CProximitySensor(CX3DEnviromentalSensorNode):
    m_strNodeName = "ProximitySensor"
    def __init__(self):
        self.m_strNodeName = "ProximitySensor"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass