from X3DLib import *

class CTouchSensor(CX3DTouchSensorNode):

    m_strNodeName = "TouchSensor"

    def __init__(self):
        self.DEF = ""
        self.m_Parent = [None]
        self.children = []
        self.m_toNode = [None]
        self.m_tofield = [None]

    def setDEF(self, value):
        self.DEF = value

    def getDEF(self):
        return self.DEF

    def setSource(self, value):
        self.m_tofield[0] = value

    def setToNode(self, value):
        self.m_toNode[0] = value

    def getSource(self):
        return self.m_tofield[0]

    def getToNode(self):
        return self.m_toNode[0]

    def setField(self, value):
        self.m_tofield[0] = value