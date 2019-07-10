from . import *

# HAnimJoint defines a concrete node interface that extends interfaces X3DChildNodeX3DBoundedObject.
class CHAnimJoint(CX3DGroupingNode):
    m_strNodeName = "HAnimJoint"
    def __init__(self):
        self.m_strNodeName = "HAnimJoint"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return String result from jointNames type inputOutput field named "name"
    def getName (self):
        pass

    # Assign String value to jointNames type inputOutput field named "name"
    def setName (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "center"
    def getCenter (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "center"
    def setCenter (self, value):
        pass

    # Return array of 4-tuple float results array in radians from SFRotation inputOutput field named "rotation"
    def getRotation (self):
        pass

    # Assign 4-tuple float array in radians to SFRotation inputOutput field named "rotation"
    def setRotation (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "scale"
    def getScale (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "scale"
    def setScale (self, value):
        pass

    # Return array of 4-tuple float results array in radians from SFRotation inputOutput field named "scaleOrientation"
    def getScaleOrientation (self):
        pass

    # Assign 4-tuple float array in radians to SFRotation inputOutput field named "scaleOrientation"
    def setScaleOrientation (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "translation"
    def getTranslation (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "translation"
    def setTranslation (self, value):
        pass

    # Return MFInt32 result [] from MFInt32 inputOutput field named "skinCoordIndex"
    def getSkinCoordIndex (self):
        pass

    # Return number of primitive values in "skinCoordIndex" array
    def getNumSkinCoordIndex (self):
        pass

    # Assign MFInt32 value [] to MFInt32 inputOutput field named "skinCoordIndex"
    def setSkinCoordIndex1 (self, values, size):
        pass

    # Assign single SFInt32 value [] as the MFInt32 array for inputOutput field named "skinCoordIndex"
    def setSkinCoordIndex2 (self, value):
        pass

    # Return array of float results array [] from MFFloat inputOutput field named "skinCoordWeight"
    def getSkinCoordWeight (self):
        pass

    # Return number of primitive values in "skinCoordWeight" array
    def getNumSkinCoordWeight (self):
        pass

    # Assign float array [] to MFFloat inputOutput field named "skinCoordWeight"
    def setSkinCoordWeight1 (self, values, size):
        pass

    # Assign single float value [] as the MFFloat array for inputOutput field named "skinCoordWeight"
    def setSkinCoordWeight2 (self, value):
        pass

    # Return array of float results array [] from MFFloat inputOutput field named "llimit"
    def getLlimit (self):
        pass

    # Return number of primitive values in "llimit" array
    def getNumLlimit (self):
        pass

    # Assign float array [] to MFFloat inputOutput field named "llimit"
    def setLlimit1 (self, values, size):
        pass

    # Assign single float value [] as the MFFloat array for inputOutput field named "llimit"
    def setLlimit2 (self, value):
        pass

    # Return array of float results array [] from MFFloat inputOutput field named "ulimit"
    def getUlimit (self):
        pass

    # Return number of primitive values in "ulimit" array
    def getNumUlimit (self):
        pass

    # Assign float array [] to MFFloat inputOutput field named "ulimit"
    def setUlimit1 (self, values, size):
        pass

    # Assign single float value [] as the MFFloat array for inputOutput field named "ulimit"
    def setUlimit2 (self, value):
        pass

    # Return array of 4-tuple float results array in radians from SFRotation inputOutput field named "limitOrientation"
    def getLimitOrientation (self):
        pass

    # Assign 4-tuple float array in radians to SFRotation inputOutput field named "limitOrientation"
    def setLimitOrientation (self, value):
        pass

    # Return array of float results array [] from MFFloat inputOutput field named "stiffness"
    def getStiffness (self):
        pass

    # Return number of primitive values in "stiffness" array
    def getNumStiffness (self):
        pass

    # Assign float array [] to MFFloat inputOutput field named "stiffness"
    def setStiffness1 (self, values, size):
        pass

    # Assign single float value [] as the MFFloat array for inputOutput field named "stiffness"
    def setStiffness2 (self, value):
        pass

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

    # Assign HAnimJoint|HAnimSegment array (using a properly typed node array) to MFNode inputOnly field named "addChildren"
    def addChildren1 (self, nodes):
        pass

    # Assign single X3DNode[] value (using a properly typed node) as the MFNode array for inputOnly field named "addChildren"
    def addChildren2 (self, node):
        pass

    # Assign HAnimJoint|HAnimSegment array (using a properly typed protoInstance array) to MFNode inputOnly field named "addChildren"
    def addChildren3 (self, node):
        pass

    # Assign HAnimJoint|HAnimSegment array (using a properly typed node array) to MFNode inputOnly field named "removeChildren"
    def removeChildren1 (self, nodes):
        pass

    # Assign single X3DNode[] value (using a properly typed node) as the MFNode array for inputOnly field named "removeChildren"
    def removeChildren2 (self, node):
        pass

    # Assign HAnimJoint|HAnimSegment array (using a properly typed protoInstance array) to MFNode inputOnly field named "removeChildren"
    def removeChildren3 (self, node):
        pass

    # Return array of HAnimJoint|HAnimSegment results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "children"
    def getChildren (self, result):
        pass

    # Return number of nodes in "children" array
    def getNumChildren (self):
        pass

    # Assign HAnimJoint|HAnimSegment array (using a properly typed node array) to MFNode inputOutput field named "children"
    def setChildren1 (self, nodes):
        pass

    # Assign single X3DNode[] value (using a properly typed node) as the MFNode array for inputOutput field named "children"
    def setChildren2 (self, node):
        pass

    # Assign HAnimJoint|HAnimSegment array (using a properly typed protoInstance array) to MFNode inputOutput field named "children"
    def setChildren3 (self, node):
        pass

    # Return array of HAnimDisplacer results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "displacers"
    def getDisplacers (self, result):
        pass

    # Return number of nodes in "displacers" array
    def getNumDisplacers (self):
        pass

    # Assign HAnimDisplacer array (using a properly typed node array) to MFNode inputOutput field named "displacers"
    def setDisplacers1 (self, nodes):
        pass

    # Assign single HAnimDisplacer value (using a properly typed node) as the MFNode array for inputOutput field named "displacers"
    def setDisplacers2 (self, node):
        pass

    # Assign HAnimDisplacer array (using a properly typed protoInstance array) to MFNode inputOutput field named "displacers"
    def setDisplacers3 (self, node):
        pass

    # Assign HAnimDisplacer array (using a properly typed node array) to MFNode inputOutput field named "displacers"
    def setDisplacers (self, nodes):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return X3DMetadataObject result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "metadata"
    def getMetadata (self):
        pass

    # Assign X3DMetadataObject value (using a properly typed node) to SFNode inputOutput field named "metadata"
    def setMetadata1 (self, node):
        pass

    # Assign X3DMetadataObject value (using a properly typed protoInstance)
    def setMetadata2 (self, protoInstance):
        pass
    #