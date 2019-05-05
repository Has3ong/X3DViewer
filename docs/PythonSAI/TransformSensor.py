from . import *

class CTransformSensor(CX3DEnviromentalSensorNode):
    m_strNodeName = "TransformSensor"
    def __init__(self):
        self.m_strNodeName = "TransformSensor"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass