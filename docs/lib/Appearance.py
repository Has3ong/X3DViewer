from X3DLib import *

class CAppearance(CX3DAppearanceNode):
    m_strNodeName = "Appearance"
    DEF = ""

    material = []
    imagetexture = []

    def setMaterial(self, node):
        self.material = node

    def setImageTexture(self, node):
        self.imagetexture = node