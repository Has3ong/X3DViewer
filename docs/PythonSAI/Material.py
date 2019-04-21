from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from . import *

class CMaterial(CX3DMaterialNode):
    m_strNodeName = "Material"
    DEF = ""

    diffuseColor = [0.8, 0.8, 0.8]
    emissiveColor = [0.0, 0.0, 0.0]
    specularColor = [0.0, 0.0, 0.0]

    ambientIntensity = 0.2
    shininess = 0.2
    transparency = 0

    def __init__(self):
        self.DEF = [""]
        self.diffuseColor = [0.8, 0.8, 0.8]
        self.m_fromNode = [None]

    def Draw(self):
        material_shininess = 0.0
        material_shininess = self.shininess * 128

        glColor3f(self.diffuseColor[0], self.diffuseColor[1], self.diffuseColor[2])
        
    def setDiffuseColor1(self, color):
        self.diffuseColor[0] = color[0]
        self.diffuseColor[1] = color[1]
        self.diffuseColor[2] = color[2]

    def setDiffuseColor2(self, val):
        self.diffuseColor[0] = val.r()
        self.diffuseColor[1] = val.g()
        self.diffuseColor[2] = val.b()

    def getDiffuseColor(self):
        return self.diffuseColor

    def setEmissiveColor1(self, color):
        self.emissiveColor[0] = color[0]
        self.emissiveColor[1] = color[1]
        self.emissiveColor[2] = color[2]

    def setEmissiveColor2(self, val):
        self.emissiveColor[0] = val.r()
        self.emissiveColor[1] = val.g()
        self.emissiveColor[2] = val.b()

    def getEmissiveColor(self):
        return self.emissiveColor

    def setSpecularColor1(self, color):
        self.specularColor[0] = color[0]
        self.specularColor[1] = color[1]
        self.specularColor[2] = color[2]

    def setSpecularColor2(self, val):
        self.specularColor[0] = val.r()
        self.specularColor[1] = val.g()
        self.specularColor[2] = val.b()
        
    def getSpecularColor(self):
        return self.specularColor

    def setAmbientIntensity(self, value):
        self.ambientIntensity = value
    
    def getAmbientIntensity(self):
        return self.ambientIntensity

    def setShininess(self, value):
        self.shininess = value

    def getShininess(self):
        return self.shininess

    def setTransparency(self, value):
        self.transparency = value

    def getTransparency(self):
        return self.transparency