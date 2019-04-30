from . import *

class CX3DUrlObject(CX3DNode):
    url = ""

    def __init__(self):
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.url = ""

    def setURL(self, value):
        self.url = value

    def getURL(self):
        return self.url
