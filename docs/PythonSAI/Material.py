from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from . import *

# Material defines a concrete node interface that extends interface X3DMaterialNode.
class CMaterial(CX3DMaterialNode):
    m_strNodeName = "Material"

    diffuseColor = [0.7, 0.7, 0.7]
    emissiveColor = [0.0, 0.0, 0.0]
    specularColor = [0.0, 0.0, 0.0]

    ambientIntensity = 0.2
    shininess = 0.2
    transparency = 0
    def __init__(self):
        self.m_strNodeName = "Material"
        self.m_Parent = [None]
        self.children = []
        self.SourceNode = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0
 
        self.diffuseColor = [0.7, 0.7, 0.7]
        self.emissiveColor = [0.0, 0.0, 0.0]
        self.specularColor = [0.0, 0.0, 0.0]
        self.ambientIntensity = 0.2
        self.shininess = 0.2
        self.transparency = 0
        self.m_fromNode = [None]

    # Return float result [] from intensityType type inputOutput field named "ambientIntensity"
    def getAmbientIntensity(self):
        return self.ambientIntensity

    # Assign float value [] to intensityType type inputOutput field named "ambientIntensity"
    def setAmbientIntensity(self, value):
        self.ambientIntensity = value

    # Return array of 3-tuple float results array using RGB values [0..1] from SFColor inputOutput field named "diffuseColor"
    def getDiffuseColor(self):
        return self.diffuseColor

    # Assign 3-tuple float array using RGB values [0..1] to SFColor inputOutput field named "diffuseColor"
    def setDiffuseColor(self, color):
        self.diffuseColor[0] = color.r()
        self.diffuseColor[1] = color.g()
        self.diffuseColor[2] = color.b()

    # Return array of 3-tuple float results array using RGB values [0..1] from SFColor inputOutput field named "emissiveColor"
    def getEmissiveColor(self):
        return self.emissiveColor

    # Assign 3-tuple float array using RGB values [0..1] to SFColor inputOutput field named "emissiveColor"
    def setEmissiveColor(self, color):
        self.emissiveColor[0] = color.r()
        self.emissiveColor[1] = color.g()
        self.emissiveColor[2] = color.b()

    # Return float result [] from intensityType type inputOutput field named "shininess"
    def getShininess(self):
        return self.shininess

    # Assign float value [] to intensityType type inputOutput field named "shininess"
    def setShininess(self, value):
        self.shininess = value

    # Return array of 3-tuple float results array using RGB values [0..1] from SFColor inputOutput field named "specularColor"
    def getSpecularColor(self):
        return self.specularColor

    # Assign 3-tuple float array using RGB values [0..1] to SFColor inputOutput field named "specularColor"
    def setSpecularColor(self, color):
        self.specularColor[0] = color.r()
        self.specularColor[1] = color.g()
        self.specularColor[2] = color.b()

    # Return float result [] from intensityType type inputOutput field named "transparency"
    def getTransparency(self):
        return self.transparency

    # Assign float value [] to intensityType type inputOutput field named "transparency"
    def setTransparency(self, value):
        self.transparency = value

    def Draw(self):
        material_shininess = 0.0
        material_shininess = self.shininess * 128

        glColor3f(self.diffuseColor[0], self.diffuseColor[1], self.diffuseColor[2])