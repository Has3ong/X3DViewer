from . import *

# Transform defines a concrete node interface that extends interface X3DGroupingNode.
class CTransform(CX3DGroupingNode):
    m_strNodeName = "Transform"

    center = [0.0, 0.0, 0.0]
    rotation = [0.0, 0.0, 1.0, 0.0]
    scale = [1.0, 1.0, 1.0]
    scaleOrientation = [0.0, 0.0, 1.0, 0.0]
    translation = [0.0, 0.0, 0.0]

    def __init__(self):
        self.m_strNodeName = "Transform"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

        self.center = [0.0,0.0,0.0]
        self.rotation = [0.0,0.0,1.0,0.0]
        self.scale = [1.0,1.0,1.0]
        self.scaleOrientation = [0.0,0.0,1.0,0.0]
        self.translation = [0.0,0.0,0.0]

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "center"
    def getCenter(self):
        return self.center

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "center"
    def setCenter(self, val):
        self.center[0] = val.x()
        self.center[1] = val.y()
        self.center[2] = val.z()

    # Return array of 4-tuple float results array in radians from SFRotation inputOutput field named "rotation"
    def getRotation(self):
        return self.rotation

    # Assign 4-tuple float array in radians to SFRotation inputOutput field named "rotation"
    def setRotation(self, val):
        self.rotation[0] = val.x()
        self.rotation[1] = val.y()
        self.rotation[2] = val.z()
        self.rotation[3] = val.w()

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "scale"
    def getScale(self):
        return self.scale

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "scale"
    def setScale(self, val):
        self.scale[0] = val.x()
        self.scale[1] = val.y()
        self.scale[2] = val.z()

    # Return array of 4-tuple float results array in radians from SFRotation inputOutput field named "scaleOrientation"
    def getScaleOrientation(self):
        return self.scaleOrientation

    # Assign 4-tuple float array in radians to SFRotation inputOutput field named "scaleOrientation"
    def setScaleOrientation(self, val):
        self.scaleOrientation[0] = val.x()
        self.scaleOrientation[1] = val.y()
        self.scaleOrientation[2] = val.z()
        self.scaleOrientation[3] = val.w()

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "translation"
    def getTranslateion(self, value):
        value[0] = self.translation[0]
        value[1] = self.translation[1]
        value[2] = self.translation[2]

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "translation"
    def setTranslation(self, val):
        self.translation[0] = val.x()
        self.translation[1] = val.y()
        self.translation[2] = val.z()

    def setAtturibute(self, Node):
        self.center = Node.center  
        self.rotation = Node.rotation
        self.scale = Node.scale
        self.scaleOrientation = Node.scaleOrientation
        self.translation = Node.translation

    # ===== methods for fields inherited from parent interfaces =====

    # Return array of 3-tuple float results array [] from SFVec3f initializeOnly field named "bboxCenter"
    def getBboxCenter (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f initializeOnly field named "bboxCenter"
    def setBboxCenter (self, value):
        pass

    # Return array of 3-tuple float results array [0,âˆž) or âˆ’1 âˆ’1 âˆ’1 from boundingBoxSizeType type initializeOnly field named "bboxSize"
    def getBboxSize (self):
        pass

    # Assign 3-tuple float array [0,âˆž) or âˆ’1 âˆ’1 âˆ’1 to boundingBoxSizeType type initializeOnly field named "bboxSize"
    def setBboxSize (self, value):
        pass

    # Assign X3DChildNode array (using a properly typed node array) to MFNode inputOnly field named "addChildren"
    def addChildren1 (self, nodes):
        pass

    # Assign single X3DChildNode value (using a properly typed node) as the MFNode array for inputOnly field named "addChildren"
    def addChildren2 (self, node):
        pass

    # Assign X3DChildNode array (using a properly typed protoInstance array) to MFNode inputOnly field named "addChildren"
    def addChildren3 (self, node):
        pass

    # Assign X3DChildNode array (using a properly typed node array) to MFNode inputOnly field named "addChildren"
    def addChildren4 (self, nodes):
        pass

    # Assign X3DChildNode array (using a properly typed node array) to MFNode inputOnly field named "removeChildren"
    def removeChildren1 (self, nodes):
        pass

    # Assign single X3DChildNode value (using a properly typed node) as the MFNode array for inputOnly field named "removeChildren"
    def removeChildren2 (self, node):
        pass

    # Assign X3DChildNode array (using a properly typed protoInstance array) to MFNode inputOnly field named "removeChildren"
    def removeChildren3 (self, node):
        pass

    # Assign X3DChildNode array (using a properly typed node array) to MFNode inputOnly field named "removeChildren"
    def removeChildren4 (self, nodes):
        pass

    # Return array of X3DChildNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "children"
    def getChildren (self, result):
        pass

    # Return number of nodes in "children" array
    def getNumChildren (self):
        pass

    # Assign X3DChildNode array (using a properly typed node array) to MFNode inputOutput field named "children"
    def setChildren1 (self, nodes):
        pass

    # Assign single X3DChildNode value (using a properly typed node) as the MFNode array for inputOutput field named "children"
    def setChildren2 (self, node):
        pass

    # Assign X3DChildNode array (using a properly typed protoInstance array) to MFNode inputOutput field named "children"
    def setChildren3 (self, node):
        pass

    # Assign X3DChildNode array (using a properly typed node array) to MFNode inputOutput field named "children"
    def setChildren4 (self, nodes):
        pass

    # Return X3DMetadataObject result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "metadata"
    def getMetadata (self):
        pass

    # Assign X3DMetadataObject value (using a properly typed node) to SFNode inputOutput field named "metadata"
    def setMetadata1 (self, node):
        pass

    # Assign X3DMetadataObject value (using a properly typed protoInstance)
    def setMetadata2 (self, protoInstance):
        pass