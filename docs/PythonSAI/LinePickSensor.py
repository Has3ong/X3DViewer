from . import *

class CLinePickSensor(CX3DPickSensorNode):
    m_strNodeName = "LinePickSensor"
    def __init__(self):
        self.m_strNodeName = "LinePickSensor"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass