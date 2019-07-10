from . import *

# GeoLOD defines a concrete node interface that extends interfaces X3DChildNodeX3DBoundedObject.
class CGeoLOD(CX3DChildNode):
    m_strNodeName = "GeoLOD"
    def __init__(self):
        self.m_strNodeName = "GeoLOD"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return int result [] from SFInt32 outputOnly field named "level_changed"
    def getLevel (self):
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

    # Return array of String results array [] from MFString initializeOnly field named "rootUrl"
    def getRootUrl (self):
        pass

    # Return number of primitive values in "rootUrl" array
    def getNumRootUrl (self):
        pass

    # Assign String array [] to MFString initializeOnly field named "rootUrl"
    def setRootUrl1 (self, values, size):
        pass

    # Assign single String value [] as the MFString array for initializeOnly field named "rootUrl"
    def setRootUrl2 (self, value):
        pass

    # Return array of String results array [] from MFString initializeOnly field named "child1Url"
    def getChild1Url (self):
        pass

    # Return number of primitive values in "child1Url" array
    def getNumChild1Url (self):
        pass

    # Assign String array [] to MFString initializeOnly field named "child1Url"
    def setChild1Url (self, values, size):
        pass

    # Assign single String value [] as the MFString array for initializeOnly field named "child1Url"
    def setChild2Url (self, value):
        pass

    # Return array of String results array [] from MFString initializeOnly field named "child2Url"
    def getChild2Url (self):
        pass

    # Return number of primitive values in "child2Url" array
    def getNumChild2Url (self):
        pass

    # Assign String array [] to MFString initializeOnly field named "child2Url"
    def setChild3Url (self, values, size):
        pass

    # Assign single String value [] as the MFString array for initializeOnly field named "child2Url"
    def setChild4Url (self, value):
        pass

    # Return array of String results array [] from MFString initializeOnly field named "child3Url"
    def getChild3Url (self):
        pass

    # Return number of primitive values in "child3Url" array
    def getNumChild3Url (self):
        pass

    # Assign String array [] to MFString initializeOnly field named "child3Url"
    def setChild8Url (self, values, size):
        pass

    # Assign single String value [] as the MFString array for initializeOnly field named "child3Url"
    def setChild6Url (self, value):
        pass

    # Return array of String results array [] from MFString initializeOnly field named "child4Url"
    def getChild4Url (self):
        pass

    # Return number of primitive values in "child4Url" array
    def getNumChild4Url (self):
        pass

    # Assign String array [] to MFString initializeOnly field named "child4Url"
    def setChild7Url (self, values, size):
        pass

    # Assign single String value [] as the MFString array for initializeOnly field named "child4Url"
    def setChild8Url (self, value):
        pass

    # Return array of 3-tuple double results array [] from SFVec3d inputOutput field named "center"
    def getCenter (self):
        pass

    # Assign 3-tuple double array [] to SFVec3d inputOutput field named "center"
    def setCenter (self, value):
        pass

    # Return float result [] from SFFloat initializeOnly field named "range"
    def getRange (self):
        pass

    # Assign float value [] to SFFloat initializeOnly field named "range"
    def setRange (self, value):
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

    # Return array of X3DChildNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode outputOnly field named "children"
    def getChildren (self, result):
        pass

    # Return number of nodes in "children" array
    def getNumChildren (self):
        pass

    # Return array of X3DChildNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode initializeOnly field named "rootNode"
    def getRootNode (self, result):
        pass

    # Return number of nodes in "rootNode" array
    def getNumRootNode (self):
        pass

    # Assign X3DChildNode array (using a properly typed node array) to MFNode initializeOnly field named "rootNode"
    def setRootNode1 (self, nodes):
        pass

    # Assign single X3DChildNode value (using a properly typed node) as the MFNode array for initializeOnly field named "rootNode"
    def setRootNode2 (self, node):
        pass

    # Assign X3DChildNode array (using a properly typed protoInstance array) to MFNode initializeOnly field named "rootNode"
    def setRootNode3 (self, node):
        pass

    # Assign X3DChildNode array (using a properly typed node array) to MFNode initializeOnly field named "rootNode"
    def setRootNode4 (self, nodes):
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

    # Return X3DMetadataObject result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "metadata"
    def getMetadata (self):
        pass

    # Assign X3DMetadataObject value (using a properly typed node) to SFNode inputOutput field named "metadata"
    def setMetadata1 (self, node):
        pass

    # Assign X3DMetadataObject value (using a properly typed protoInstance)
    def setMetadata2 (self, protoInstance):
        pass
