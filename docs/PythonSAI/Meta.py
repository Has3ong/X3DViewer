from . import *

class CMeta(CX3DNode):
    m_strNodeName = "Meta"
    content = ""
    name = ""

    def setContent(self, value):
        self.content = value

    def setName(self, value):
        self.name = value