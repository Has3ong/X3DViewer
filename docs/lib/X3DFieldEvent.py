from X3DLib import *

class X3DFieldEvent():

    m_value = ""

    def __init__(self):
        self.m_value = ""

    def getTime(self):
        return 0

    def getSource(self):
        return self.m_value