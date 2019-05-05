from . import *

class CSliderJoint(CX3DRigidJointNode):
    m_strNodeName = "SliderJoint"
    def __init__(self):
        self.m_strNodeName = "SliderJoint"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
    pass