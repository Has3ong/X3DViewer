from . import *

class CAppearance(CX3DAppearanceNode):
    m_strNodeName = "Appearance"
    material = []
    texture = []
    textureTransform = []
    shaders = []
    def __init__(self):
        self.m_strNodeName = "Appearance"
        self.material = []
        self.texture = []
        self.textureTransform = []
        self.shaders = []
        
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

    def setMaterial(self, node):
        self.material = node

    def setImageTexture(self, node):
        self.imagetexture = node