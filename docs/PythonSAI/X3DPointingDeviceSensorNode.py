from . import *

class CX3DPointingDeviceSensorNode(CX3DSensorNode):
    m_strNodeName = "CX3DPointingDeviceSensorNode"
    def __init__(self):
        self.m_strNodeName = "X3DPointingDeviceSensorNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass