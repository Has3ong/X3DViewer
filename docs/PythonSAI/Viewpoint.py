from . import *

class CViewpoint(CX3DViewpointNode):
    m_strNodeName = "Viewpoint"
    CONST_PI = 3.14159265
    fieldOfView = CONST_PI / 4.0
    def __init__(self):
        self.m_strNodeName = "Viewpoint"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

        self.CONST_PI = 3.14159265
        self.fieldOfView = self.CONST_PI / 4.0
        

    def setFieldOfView(self, value):
        self.fieldOfView = value

    def getFieldOfView(self):
        return self.fieldOfView
