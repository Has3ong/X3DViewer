from . import *


# EspduTransform defines a concrete node interface that extends interfaces X3DGroupingNodeX3DNetworkSensorNode.
class CEspduTransform(CX3DGroupingNode, CX3DNetworkSensorNode):
    m_strNodeName = "EspduTransform"
    def __init__(self):
        self.m_strNodeName = "EspduTransform"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Assign float value [] to SFFloat inputOnly field named "set_articulationParameterValue0"
    def setArticulationParameterValue0 (self, value):
        pass

    # Assign float value [] to SFFloat inputOnly field named "set_articulationParameterValue1"
    def setArticulationParameterValue1 (self, value):
        pass

    # Assign float value [] to SFFloat inputOnly field named "set_articulationParameterValue2"
    def setArticulationParameterValue2 (self, value):
        pass

    # Assign float value [] to SFFloat inputOnly field named "set_articulationParameterValue3"
    def setArticulationParameterValue3 (self, value):
        pass

    # Assign float value [] to SFFloat inputOnly field named "set_articulationParameterValue4"
    def setArticulationParameterValue4 (self, value):
        pass

    # Assign float value [] to SFFloat inputOnly field named "set_articulationParameterValue5"
    def setArticulationParameterValue5 (self, value):
        pass

    # Assign float value [] to SFFloat inputOnly field named "set_articulationParameterValue6"
    def setArticulationParameterValue6 (self, value):
        pass

    # Assign float value [] to SFFloat inputOnly field named "set_articulationParameterValue7"
    def setArticulationParameterValue7 (self, value):
        pass

    # Return float result [] from SFFloat outputOnly field named "articulationParameterValue0_changed"
    def getArticulationParameterValue0 (self):
        pass

    # Return float result [] from SFFloat outputOnly field named "articulationParameterValue1_changed"
    def getArticulationParameterValue1 (self):
        pass

    # Return float result [] from SFFloat outputOnly field named "articulationParameterValue2_changed"
    def getArticulationParameterValue2 (self):
        pass

    # Return float result [] from SFFloat outputOnly field named "articulationParameterValue3_changed"
    def getArticulationParameterValue3 (self):
        pass

    # Return float result [] from SFFloat outputOnly field named "articulationParameterValue4_changed"
    def getArticulationParameterValue4 (self):
        pass

    # Return float result [] from SFFloat outputOnly field named "articulationParameterValue5_changed"
    def getArticulationParameterValue5 (self):
        pass

    # Return float result [] from SFFloat outputOnly field named "articulationParameterValue6_changed"
    def getArticulationParameterValue6 (self):
        pass

    # Return float result [] from SFFloat outputOnly field named "articulationParameterValue7_changed"
    def getArticulationParameterValue7 (self):
        pass

    # Return double result in seconds from SFTime outputOnly field named "collideTime"
    def getCollideTime (self):
        pass

    # Return double result in seconds from SFTime outputOnly field named "detonateTime"
    def getDetonateTime (self):
        pass

    # Return double result in seconds from SFTime outputOnly field named "firedTime"
    def getFiredTime (self):
        pass

    # Return boolean result from SFBool outputOnly field named "isActive"
    def getIsActive (self):
        pass

    # Return boolean result from SFBool outputOnly field named "isCollided"
    def getIsCollided (self):
        pass

    # Return boolean result from SFBool outputOnly field named "isDetonated"
    def getIsDetonated (self):
        pass

    # Return boolean result from SFBool outputOnly field named "isNetworkReader"
    def getIsNetworkReader (self):
        pass

    # Return boolean result from SFBool outputOnly field named "isNetworkWriter"
    def getIsNetworkWriter (self):
        pass

    # Return boolean result from SFBool outputOnly field named "isRtpHeaderHeard"
    def getIsRtpHeaderHeard (self):
        pass

    # Return boolean result from SFBool outputOnly field named "isStandAlone"
    def getIsStandAlone (self):
        pass

    # Return double result in seconds from SFTime outputOnly field named "timestamp"
    def getTimestamp (self):
        pass

    # Return boolean result from SFBool inputOutput field named "enabled"
    def getEnabled (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "enabled"
    def setEnabled (self, value):
        pass

    # Return String result [] from SFString inputOutput field named "marking"
    def getMarking (self):
        pass

    # Assign String value [] to SFString inputOutput field named "marking"
    def setMarking (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "siteID"
    def getSiteID (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "siteID"
    def setSiteID (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "applicationID"
    def getApplicationID (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "applicationID"
    def setApplicationID (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "entityID"
    def getEntityID (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "entityID"
    def setEntityID (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "forceID"
    def getForceID (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "forceID"
    def setForceID (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "entityKind"
    def getEntityKind (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "entityKind"
    def setEntityKind (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "entityDomain"
    def getEntityDomain (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "entityDomain"
    def setEntityDomain (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "entityCountry"
    def getEntityCountry (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "entityCountry"
    def setEntityCountry (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "entityCategory"
    def getEntityCategory (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "entityCategory"
    def setEntityCategory (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "entitySubcategory"
    def getEntitySubcategory (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "entitySubcategory"
    def setEntitySubcategory (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "entitySpecific"
    def getEntitySpecific (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "entitySpecific"
    def setEntitySpecific (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "entityExtra"
    def getEntityExtra (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "entityExtra"
    def setEntityExtra (self, value):
        pass

    # Return double result in seconds from SFTime inputOutput field named "readInterval"
    def getReadInterval (self):
        pass

    # Assign double value in seconds to SFTime inputOutput field named "readInterval"
    def setReadInterval (self, timestamp):
        pass

    # Return double result in seconds from SFTime inputOutput field named "writeInterval"
    def getWriteInterval (self):
        pass

    # Assign double value in seconds to SFTime inputOutput field named "writeInterval"
    def setWriteInterval (self, timestamp):
        pass

    # Return String enumeration result ("standAlone"|"networkReader"|"networkWriter") from networkModeValues type inputOutput field named "networkMode"
    def getNetworkMode (self):
        pass

    # Assign String enumeration value ("standAlone"|"networkReader"|"networkWriter") to networkModeValues type inputOutput field named "networkMode"
    def setNetworkMode (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "translation"
    def getTranslation (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "translation"
    def setTranslation (self, value):
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

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "center"
    def getCenter (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "center"
    def setCenter (self, value):
        pass

    # Return String result [] from SFString inputOutput field named "address"
    def getAddress (self):
        pass

    # Assign String value [] to SFString inputOutput field named "address"
    def setAddress (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "port"
    def getPort (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "port"
    def setPort (self, value):
        pass

    # Return String result [] from SFString inputOutput field named "multicastRelayHost"
    def getMulticastRelayHost (self):
        pass

    # Assign String value [] to SFString inputOutput field named "multicastRelayHost"
    def setMulticastRelayHost (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "multicastRelayPort"
    def getMulticastRelayPort (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "multicastRelayPort"
    def setMulticastRelayPort (self, value):
        pass

    # Return boolean result from SFBool initializeOnly field named "rtpHeaderExpected"
    def getRtpHeaderExpected (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "rtpHeaderExpected"
    def setRtpHeaderExpected (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "deadReckoning"
    def getDeadReckoning (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "deadReckoning"
    def setDeadReckoning (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "linearVelocity"
    def getLinearVelocity (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "linearVelocity"
    def setLinearVelocity (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "linearAcceleration"
    def getLinearAcceleration (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "linearAcceleration"
    def setLinearAcceleration (self, value):
        pass

    # Return boolean result from SFBool inputOutput field named "fired1"
    def getFired1 (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "fired1"
    def setFired1 (self, value):
        pass

    # Return boolean result from SFBool inputOutput field named "fired2"
    def getFired2 (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "fired2"
    def setFired3 (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "collisionType"
    def getCollisionType (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "collisionType"
    def setCollisionType (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "detonationLocation"
    def getDetonationLocation (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "detonationLocation"
    def setDetonationLocation (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "detonationRelativeLocation"
    def getDetonationRelativeLocation (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "detonationRelativeLocation"
    def setDetonationRelativeLocation (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "detonationResult"
    def getDetonationResult (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "detonationResult"
    def setDetonationResult (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "eventApplicationID"
    def getEventApplicationID (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "eventApplicationID"
    def setEventApplicationID (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "eventEntityID"
    def getEventEntityID (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "eventEntityID"
    def setEventEntityID (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "eventNumber"
    def getEventNumber (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "eventNumber"
    def setEventNumber (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "eventSiteID"
    def getEventSiteID (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "eventSiteID"
    def setEventSiteID (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "munitionStartPoint"
    def getMunitionStartPoint (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "munitionStartPoint"
    def setMunitionStartPoint (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "munitionEndPoint"
    def getMunitionEndPoint (self):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "munitionEndPoint"
    def setMunitionEndPoint (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "munitionSiteID"
    def getMunitionSiteID (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "munitionSiteID"
    def setMunitionSiteID (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "munitionApplicationID"
    def getMunitionApplicationID (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "munitionApplicationID"
    def setMunitionApplicationID (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "munitionEntityID"
    def getMunitionEntityID (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "munitionEntityID"
    def setMunitionEntityID (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "fireMissionIndex"
    def getFireMissionIndex (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "fireMissionIndex"
    def setFireMissionIndex (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "warhead"
    def getWarhead (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "warhead"
    def setWarhead (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "fuse"
    def getFuse (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "fuse"
    def setFuse (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "munitionQuantity"
    def getMunitionQuantity (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "munitionQuantity"
    def setMunitionQuantity (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "firingRate"
    def getFiringRate (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "firingRate"
    def setFiringRate (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "firingRange"
    def getFiringRange (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "firingRange"
    def setFiringRange (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "articulationParameterCount"
    def getArticulationParameterCount (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "articulationParameterCount"
    def setArticulationParameterCount (self, value):
        pass

    # Return MFInt32 result [] from MFInt32 inputOutput field named "articulationParameterDesignatorArray"
    def getArticulationParameterDesignatorArray (self):
        pass

    # Return number of primitive values in "articulationParameterDesignatorArray" array
    def getNumArticulationParameterDesignatorArray (self):
        pass

    # Assign MFInt32 value [] to MFInt32 inputOutput field named "articulationParameterDesignatorArray"
    def setArticulationParameterDesignatorArray1 (self, values, size):
        pass

    # Assign single SFInt32 value [] as the MFInt32 array for inputOutput field named "articulationParameterDesignatorArray"
    def setArticulationParameterDesignatorArray2 (self, value):
        pass

    # Return MFInt32 result [] from MFInt32 inputOutput field named "articulationParameterChangeIndicatorArray"
    def getArticulationParameterChangeIndicatorArray (self):
        pass

    # Return number of primitive values in "articulationParameterChangeIndicatorArray" array
    def getNumArticulationParameterChangeIndicatorArray (self):
        pass

    # Assign MFInt32 value [] to MFInt32 inputOutput field named "articulationParameterChangeIndicatorArray"
    def setArticulationParameterChangeIndicatorArray1 (self, values, size):
        pass

    # Assign single SFInt32 value [] as the MFInt32 array for inputOutput field named "articulationParameterChangeIndicatorArray"
    def setArticulationParameterChangeIndicatorArray2 (self, value):
        pass

    # Return MFInt32 result [] from MFInt32 inputOutput field named "articulationParameterIdPartAttachedToArray"
    def getArticulationParameterIdPartAttachedToArray (self):
        pass

    # Return number of primitive values in "articulationParameterIdPartAttachedToArray" array
    def getNumArticulationParameterIdPartAttachedToArray (self):
        pass

    # Assign MFInt32 value [] to MFInt32 inputOutput field named "articulationParameterIdPartAttachedToArray"
    def setArticulationParameterIdPartAttachedToArray1 (self, values, size):
        pass

    # Assign single SFInt32 value [] as the MFInt32 array for inputOutput field named "articulationParameterIdPartAttachedToArray"
    def setArticulationParameterIdPartAttachedToArray2 (self, value):
        pass

    # Return MFInt32 result [] from MFInt32 inputOutput field named "articulationParameterTypeArray"
    def getArticulationParameterTypeArray (self):
        pass

    # Return number of primitive values in "articulationParameterTypeArray" array
    def getNumArticulationParameterTypeArray (self):
        pass

    # Assign MFInt32 value [] to MFInt32 inputOutput field named "articulationParameterTypeArray"
    def setArticulationParameterTypeArray1 (self, values, size):
        pass

    # Assign single SFInt32 value [] as the MFInt32 array for inputOutput field named "articulationParameterTypeArray"
    def setArticulationParameterTypeArray2 (self, value):
        pass

    # Return array of float results array [] from MFFloat inputOutput field named "articulationParameterArray"
    def getArticulationParameterArray (self):
        pass

    # Return number of primitive values in "articulationParameterArray" array
    def getNumArticulationParameterArray (self):
        pass

    # Assign float array [] to MFFloat inputOutput field named "articulationParameterArray"
    def setArticulationParameterArray1 (self, values, size):
        pass

    # Assign single float value [] as the MFFloat array for inputOutput field named "articulationParameterArray"
    def setArticulationParameterArray2 (self, value):
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

    # Return array of 3-tuple double results array [] from SFVec3d inputOutput field named "geoCoords"
    def getGeoCoords (self):
        pass

    # Assign 3-tuple double array [] to SFVec3d inputOutput field named "geoCoords"
    def setGeoCoords (self, value):
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
