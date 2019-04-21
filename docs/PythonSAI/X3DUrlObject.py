from . import *

class CX3DUrlObject(CX3DNode):
    url = ""

    def __init__(self):
        self.url = ""

    def setURL(self, value):
        self.url = value

    def getURL(self):
        return self.url
