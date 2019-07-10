from . import *

# HAnimHumanoid defines a concrete node interface that extends interfaces X3DChildNodeX3DBoundedObject.
class CHAnimHumanoid(CX3DChildNode):
    m_strNodeName = "HAnimHumanoid"
    def __init__(self):
        self.m_strNodeName = "HAnimHumanoid"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return String result [] from SFString inputOutput field named "name"
    def getName (self):
        pass

    # Assign String value [] to SFString inputOutput field named "name"
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

    # Return array of String results array [] from MFString inputOutput field named "info"
    def getInfo (self):
        pass

    # Return number of primitive values in "info" array
    def getNumInfo (self):
        pass

    # Assign String array [] to MFString inputOutput field named "info"
    def setInfo1 (self, values, size):
        pass

    # Assign single String value [] as the MFString array for inputOutput field named "info"
    def setInfo2 (self, value):
        pass

    # Return String result [] from hanimVersionValues type inputOutput field named "version"
    def getVersion (self):
        pass

    # Assign String value [] to hanimVersionValues type inputOutput field named "version"
    def setVersion (self, value):
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

    # Return array of HAnimJoint results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "joints"
    def getJoints (self, result):
        pass

    # Return number of nodes in "joints" array
    def getNumJoints (self):
        pass

    # Assign HAnimJoint array (using a properly typed node array) to MFNode inputOutput field named "joints"
    def setJoints1 (self, nodes):
        pass

    # Assign single HAnimJoint value (using a properly typed node) as the MFNode array for inputOutput field named "joints"
    def setJoints2 (self, node):
        pass

    # Assign HAnimJoint array (using a properly typed protoInstance array) to MFNode inputOutput field named "joints"
    def setJoints3 (self, node):
        pass

    # Assign HAnimJoint array (using a properly typed node array) to MFNode inputOutput field named "joints"
    def setJoints4 (self, nodes):
        pass

    # Return array of HAnimSegment results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "segments"
    def getSegments (self, result):
        pass

    # Return number of nodes in "segments" array
    def getNumSegments (self):
        pass

    # Assign HAnimSegment array (using a properly typed node array) to MFNode inputOutput field named "segments"
    def setSegments1 (self, nodes):
        pass

    # Assign single HAnimSegment value (using a properly typed node) as the MFNode array for inputOutput field named "segments"
    def setSegments2 (self, node):
        pass

    # Assign HAnimSegment array (using a properly typed protoInstance array) to MFNode inputOutput field named "segments"
    def setSegments3 (self, node):
        pass

    # Assign HAnimSegment array (using a properly typed node array) to MFNode inputOutput field named "segments"
    def setSegments4 (self, nodes):
        pass

    # Return array of HAnimSite results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "sites"
    def getSites (self, result):
        pass

    # Return number of nodes in "sites" array
    def getNumSites (self):
        pass

    # Assign HAnimSite array (using a properly typed node array) to MFNode inputOutput field named "sites"
    def setSites1 (self, nodes):
        pass

    # Assign single HAnimSite value (using a properly typed node) as the MFNode array for inputOutput field named "sites"
    def setSites2 (self, node):
        pass

    # Assign HAnimSite array (using a properly typed protoInstance array) to MFNode inputOutput field named "sites"
    def setSites3 (self, node):
        pass

    # Assign HAnimSite array (using a properly typed node array) to MFNode inputOutput field named "sites"
    def setSites4 (self, nodes):
        pass

    # Return array of HAnimJoint|HAnimSite results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "skeleton"
    def getSkeleton (self, result):
        pass

    # Return number of nodes in "skeleton" array
    def getNumSkeleton (self):
        pass

    # Assign HAnimJoint|HAnimSite array (using a properly typed node array) to MFNode inputOutput field named "skeleton"
    def setSkeleton1 (self, nodes):
        pass

    # Assign single X3DNode[] value (using a properly typed node) as the MFNode array for inputOutput field named "skeleton"
    def setSkeleton2 (self, node):
        pass

    # Assign HAnimJoint|HAnimSite array (using a properly typed protoInstance array) to MFNode inputOutput field named "skeleton"
    def setSkeleton3 (self, node):
        pass

    # Return array of X3DChildNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "skin"
    def getSkin (self, result):
        pass

    # Return number of nodes in "skin" array
    def getNumSkin (self):
        pass

    # Assign X3DChildNode array (using a properly typed node array) to MFNode inputOutput field named "skin"
    def setSkin1 (self, nodes):
        pass

    # Assign single X3DChildNode value (using a properly typed node) as the MFNode array for inputOutput field named "skin"
    def setSkin2 (self, node):
        pass

    # Assign X3DChildNode array (using a properly typed protoInstance array) to MFNode inputOutput field named "skin"
    def setSkin3 (self, node):
        pass

    # Assign X3DChildNode array (using a properly typed node array) to MFNode inputOutput field named "skin"
    def setSkin4 (self, nodes):
        pass

    # Return array of X3DCoordinateNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "skinCoord"
    def getSkinCoord (self, result):
        pass

    # Return number of nodes in "skinCoord" array
    def getNumSkinCoord (self):
        pass

    # Assign X3DCoordinateNode array (using a properly typed node array) to MFNode inputOutput field named "skinCoord"
    def setSkinCoord1 (self,  nodes):
        pass

    # Assign single X3DCoordinateNode value (using a properly typed node) as the MFNode array for inputOutput field named "skinCoord"
    def setSkinCoord2 (self, node):
        pass

    # Assign X3DCoordinateNode array (using a properly typed protoInstance array) to MFNode inputOutput field named "skinCoord"
    def setSkinCoord3 (self, node):
        pass

    # Assign X3DCoordinateNode array (using a properly typed node array) to MFNode inputOutput field named "skinCoord"
    def setSkinCoord4 (self, nodes):
        pass

    # Return array of X3DNormalNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "skinNormal"
    def getSkinNormal (self, result):
        pass

    # Return number of nodes in "skinNormal" array
    def getNumSkinNormal (self):
        pass

    # Assign X3DNormalNode array (using a properly typed node array) to MFNode inputOutput field named "skinNormal"
    def setSkinNormal1 (self, nodes):
        pass

    # Assign single X3DNormalNode value (using a properly typed node) as the MFNode array for inputOutput field named "skinNormal"
    def setSkinNormal2 (self, node):
        pass

    # Assign X3DNormalNode array (using a properly typed protoInstance array) to MFNode inputOutput field named "skinNormal"
    def setSkinNormal3 (self, node):
        pass

    # Assign X3DNormalNode array (using a properly typed node array) to MFNode inputOutput field named "skinNormal"
    def setSkinNormal4 (self, nodes):
        pass

    # Return array of HAnimSite results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "viewpoints"
    def getViewpoints (self, result):
        pass

    # Return number of nodes in "viewpoints" array
    def getNumViewpoints (self):
        pass

    # Assign HAnimSite array (using a properly typed node array) to MFNode inputOutput field named "viewpoints"
    def setViewpoints1 (self, nodes):
        pass

    # Assign single HAnimSite value (using a properly typed node) as the MFNode array for inputOutput field named "viewpoints"
    def setViewpoints2 (self, node):
        pass

    # Assign HAnimSite array (using a properly typed protoInstance array) to MFNode inputOutput field named "viewpoints"
    def setViewpoints3 (self, node):
        pass

    # Assign HAnimSite array (using a properly typed node array) to MFNode inputOutput field named "viewpoints"
    def setViewpoints4 (self, nodes):
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
