from . import *

class CAppearance(CX3DAppearanceNode):
    m_strNodeName = "Appearance"
    material = []
    imagetexture = []

    def __init__(self):
        self.m_Parent = [None]
        self.children = []
        self.SourceNode = []
        self.DEF = ""
        self.USE = ""

    def setMaterial(self, node):
        self.material = node

    def setImageTexture(self, node):
        self.imagetexture = node