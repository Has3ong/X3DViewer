from . import *

class CX3DDragSensorNode(CX3DPointingDeviceSensorNode):
    m_strNodeName = "X3DDragSensorNode"
    def __init__(self):
        self.m_strNodeName = "X3DDragSensorNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass