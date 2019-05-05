from . import *

class CCollisionSensor(CX3DSensorNode):
    m_strNodeName = "CollisionSensor"
    def __init__(self):
        self.m_strNodeName = "CollisionSensor"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass