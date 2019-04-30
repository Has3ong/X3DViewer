from . import *

class CX3DBindableNode(CX3DChildNode):
    m_strNodeName = "X3DBindanbleNode"
    bound = True
    bindTime = 0.0

    def setBind(self, value):
        self.bound = value

    def getBindTime(self):
        return self.bindTime

    def getIsBound(self):
        return self.bound