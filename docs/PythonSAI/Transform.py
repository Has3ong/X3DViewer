from . import *

class CTransform(CX3DGroupingNode):
    m_strNodeName = "Transform"

    center = [0.0, 0.0, 0.0]
    rotation = [0.0, 0.0, 1.0, 0.0]
    scale = [1.0, 1.0, 1.0]
    scaleOrientation = [0.0, 0.0, 1.0, 0.0]
    translation = [0.0, 0.0, 0.0]

    def __init__(self):
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.center = [0.0,0.0,0.0]
        self.rotation = [0.0,0.0,1.0,0.0]
        self.scale = [1.0,1.0,1.0]
        self.scaleOrientation = [0.0,0.0,1.0,0.0]
        self.translation = [0.0,0.0,0.0]
        
    def getCenter(self, value):
        value[0] = self.center[0]
        value[1] = self.center[1]
        value[2] = self.center[2]

    def setCenter1(self, value):
        self.center[0] = value[0]
        self.center[1] = value[1]
        self.center[2] = value[2]

    def setCenter2(self, val):
        self.center[0] = val.x()
        self.center[1] = val.y()
        self.center[2] = val.z()

    def getRotation(self, value):
        value[0] = self.rotation[0]
        value[1] = self.rotation[1]
        value[2] = self.rotation[2]
        value[3] = self.rotation[3]

    def setRotation1(self, value):
        self.rotation[0] = value[0]
        self.rotation[1] = value[1]
        self.rotation[2] = value[2]
        self.rotation[3] = value[3]

    def setRotation2(self, val):
        self.rotation[0] = val.x()
        self.rotation[1] = val.y()
        self.rotation[2] = val.z()
        self.rotation[3] = val.w()

    def getScale(self, value):
        value[0] = self.scale[0]
        value[1] = self.scale[1]
        value[2] = self.scale[2]

    def setScale1(self, value):
        self.scale[0] = value[0]
        self.scale[1] = value[1]
        self.scale[2] = value[2]

    def setScale2(self, val):
        self.scale[0] = val.x()
        self.scale[1] = val.y()
        self.scale[2] = val.z()

    def getScaleOrientation(self, value):
        value[0] = self.scaleOrientation[0]
        value[1] = self.scaleOrientation[1]
        value[2] = self.scaleOrientation[2]
        value[3] = self.scaleOrientation[3]

    def setScaleOrientation1(self, value):
        self.scaleOrientation[0] = value[0]
        self.scaleOrientation[1] = value[1]
        self.scaleOrientation[2] = value[2]
        self.scaleOrientation[3] = value[3]

    def setScaleOrientation2(self, val):
        self.scaleOrientation[0] = val.x()
        self.scaleOrientation[1] = val.y()
        self.scaleOrientation[2] = val.z()
        self.scaleOrientation[3] = val.w()

    def getTranslateion(self, value):
        value[0] = self.translation[0]
        value[1] = self.translation[1]
        value[2] = self.translation[2]

    def setTranslation1(self, value):
        self.translation[0] = value[0]
        self.translation[1] = value[1]
        self.translation[2] = value[2]

    def setTranslation2(self, val):
        self.translation[0] = val.x()
        self.translation[1] = val.y()
        self.translation[2] = val.z()