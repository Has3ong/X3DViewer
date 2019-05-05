from . import *

class CVisibilitySensor(CX3DEnviromentalSensorNode):
    m_strNodeName = "VisibilitySensor"
    def __init__(self):
        self.m_strNodeName = "VisibilitySensor"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass