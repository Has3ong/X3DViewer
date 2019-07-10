from . import *

# LinePickSensor defines a concrete node interface that extends interface X3DPickSensorNode.
class CLinePickSensor(CX3DPickSensorNode):
    m_strNodeName = "LinePickSensor"
    def __init__(self):
        self.m_strNodeName = "LinePickSensor"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of 3-tuple float results array [] from MFVec3f outputOnly field named "pickedNormal"
    def getPickedNormal (self):
        pass

    # Return number of 3-tuple primitive values in "pickedNormal" array
    def getNumPickedNormal (self):
        pass

    # Return array of 3-tuple float results array [] from MFVec3f outputOnly field named "pickedPoint"
    def getPickedPoint (self, result, size):
        pass

    # Return number of 3-tuple primitive values in "pickedPoint" array
    def getNumPickedPoint (self):
        pass

    # Return array of 3-tuple float results array [] from MFVec3f outputOnly field named "pickedTextureCoordinate"
    def getPickedTextureCoordinate (self, result, size):
        pass

    # Return number of 3-tuple primitive values in "pickedTextureCoordinate" array
    def getNumPickedTextureCoordinate (self):
        pass

    #   // ===== methods for fields inherited from parent interfaces =====
    #
    # Return boolean result from SFBool outputOnly field named "isActive"
    def getIsActive (self):
        pass

    # Return boolean result from SFBool inputOutput field named "enabled"
    def getEnabled (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "enabled"
    def setEnabled (self, value):
        pass

    # Return array of String results array ["ALL","NONE","TERRAIN",...] from MFString inputOutput field named "objectType"
    def getObjectType (self):
        pass

    # Return number of primitive values in "objectType" array
    def getNumObjectType (self):
        pass

    # Assign String array ["ALL","NONE","TERRAIN",...] to MFString inputOutput field named "objectType"
    def setObjectType1 (self, values, size):
        pass

    # Assign single String value ["ALL","NONE","TERRAIN",...] as the MFString array for inputOutput field named "objectType"
    def setObjectType2 (self, value):
        pass

    # Return String result (enumeration values "GEOMETRY"|"BOUNDS"|...) from SFString initializeOnly field named "intersectionType"
    def getIntersectionType (self):
        pass

    # Assign String value (enumeration values "GEOMETRY"|"BOUNDS"|...) to SFString initializeOnly field named "intersectionType"
    def setIntersectionType (self, value):
        pass

    # Return String result ["ANY"|"CLOSEST"|"ALL"|"ALL_SORTED"] from  type initializeOnly field named "sortOrder"
    def getSortOrder (self):
        pass

    # Assign String value ["ANY"|"CLOSEST"|"ALL"|"ALL_SORTED"] to  type initializeOnly field named "sortOrder"
    def setSortOrder (self, value):
        pass

    # Return array of X3DGroupingNode|X3DShapeNode|Inline results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "pickTarget"
    def getPickTarget (self, result):
        pass

    # Return number of nodes in "pickTarget" array
    def getNumPickTarget (self):
        pass

    # Assign X3DGroupingNode|X3DShapeNode|Inline array (using a properly typed node array) to MFNode inputOutput field named "pickTarget"
    def setPickTarget1 (self, nodes):
        pass

    # Assign single X3DNode[] value (using a properly typed node) as the MFNode array for inputOutput field named "pickTarget"
    def setPickTarget2 (self, node):
        pass

    # Assign X3DGroupingNode|X3DShapeNode|Inline array (using a properly typed protoInstance array) to MFNode inputOutput field named "pickTarget"
    def setPickTarget3 (self, node):
        pass

    # Return array of X3DChildNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode outputOnly field named "pickedGeometry"
    def getPickedGeometry (self, result):
        pass

    # Return number of nodes in "pickedGeometry" array
    def getNumPickedGeometry (self):
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

    # Return X3DGeometryNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "pickingGeometry"
    def getPickingGeometry (self, result):
        pass

    # Assign X3DGeometryNode value (using a properly typed node) to SFNode inputOutput field named "pickingGeometry"
    def setPickingGeometry1 (self, node):
        pass

    # Assign X3DGeometryNode value (using a properly typed protoInstance)
    def setPickingGeometry2 (self, protoInstance):
        pass
