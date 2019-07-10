from . import *

# GeoTransform defines a concrete node interface that extends interface X3DGroupingNode.
class CGeoTransform(CX3DGroupingNode):
    m_strNodeName = "GeoTransform"
    def __init__(self):
        self.m_strNodeName = "GeoTransform"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of 3-tuple double results array [] from SFVec3d inputOutput field named "geoCenter"
    def getGeoCenter (self):
        pass

    # Assign 3-tuple double array [] to SFVec3d inputOutput field named "geoCenter"
    def setGeoCenter (self, value):
        pass

    # Return array of String results array [] from geoSystemType type initializeOnly field named "geoSystem"
    def getGeoSystem (self):
        pass

    # Return number of primitive values in "geoSystem" array
    def getNumGeoSystem (self):
        pass

    # Assign String array [] to geoSystemType type initializeOnly field named "geoSystem"
    def setGeoSystem (self, values, size):
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

    # Return GeoOrigin result (deprecated node, optional) from SFNode initializeOnly field named "geoOrigin"
    def getGeoOrigin (self, result):
        pass

    # Assign GeoOrigin value (deprecated node, optional) to SFNode initializeOnly field named "geoOrigin"
    def setGeoOrigin1 (self, node):
        pass

    # Assign GeoOrigin value (deprecated protoInstance)
    def setGeoOrigin2 (self, protoInstance):
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
