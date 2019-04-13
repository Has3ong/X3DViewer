from X3DLib import *

class CScript(CX3DScriptNode):
    m_strNodeName = "Script"
    directOutput = False
    mustEvaluate = False

    def __init__(self):
        self.url = ""
        self.DEF = ""
        self.USE = ""
        self.directOutput = False
        self.mustEvaluate = False

        self.m_tofield = [None]
        self.m_toNode = [None]

    def setDirectOutput(self, value):
        self.directOutput = value

    def getDirectOutput(self):
        return self.directOutput

    def setMustEvaluate(self, value):
        self.mustEvaluate = value

    def getMustEvaluate(self):
        return self.mustEvaluate

    def setDiffuseColor(self, value):
        mat = self.m_toNode[0]
        mat.setDiffuseColor2(value)

    def setSource(self, value):
        self.m_tofield[0] = value

    def getSource(self):
        return self.m_tofield[0]

    def setToNode(self, value):
        self.m_toNode[0] = value

    def getToNode(self):
        return self.m_toNode[0]

    def setField(self, value):
        self.m_tofield[0] = value



    