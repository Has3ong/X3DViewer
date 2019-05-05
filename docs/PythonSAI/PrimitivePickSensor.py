from . import *

class CPrimitivePickSensor(CX3DPickSensorNode):
    m_strNodeName = "PrimitivePickSensor"
    def __init__(self):
        self.m_strNodeName = "PrimitivePickSensor"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass