from . import *

# HAnimSegment defines a concrete node interface that extends interface X3DGroupingNode.
class CHAnimSegment(CX3DGroupingNode):
    m_strNodeName = "HAnimSegment"
    def __init__(self):
        self.m_strNodeName = "HAnimSegment"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return String result from segmentNames type inputOutput field named "name"
    def getName (self):
        pass

    # Assign String value to segmentNames type inputOutput field named "name"
    def setName (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "mass"
    def getMass (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "mass"
    def setMass (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "centerOfMass"
    def getCenterOfMass (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "centerOfMass"
    def setCenterOfMass (self, value):
        pass

    # Return array of float results array [] from MFFloat inputOutput field named "momentsOfInertia"
    def getMomentsOfInertia (self):
        pass

    # Return number of primitive values in "momentsOfInertia" array
    def getNumMomentsOfInertia (self):
        pass

    # Assign float array [] to MFFloat inputOutput field named "momentsOfInertia"
    def setMomentsOfInertia1 (self, values, size):
        pass

    # Assign single float value [] as the MFFloat array for inputOutput field named "momentsOfInertia"
    def setMomentsOfInertia2 (self, value):
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
    def setDisplacers4 (self, nodes):
        pass

    # Return X3DCoordinateNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "coord"
    def getCoord (self, result):
        pass

    # Assign X3DCoordinateNode value (using a properly typed node) to SFNode inputOutput field named "coord"
    def setCoord1 (self, node):
        pass

    # Assign X3DCoordinateNode value (using a properly typed protoInstance)
    def setCoord2 (self, protoInstance):
        pass

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
