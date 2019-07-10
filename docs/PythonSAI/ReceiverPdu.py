from . import *

# ReceiverPdu defines a concrete node interface that extends interfaces X3DNetworkSensorNodeX3DBoundedObject.
class CReceiverPdu(CX3DSensorNode):
    m_strNodeName = "ReceiverPdu"
    def __init__(self):
        self.m_strNodeName = "ReceiverPdu"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

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

    # Return int result [] from SFInt32 inputOutput field named "whichGeometry"
    def getWhichGeometry (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "whichGeometry"
    def setWhichGeometry (selfe, value):
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

    # Return int result [] from SFInt32 inputOutput field named "radioID"
    def getRadioID (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "radioID"
    def setRadioID (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "receivedPower"
    def getReceivedPower (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "receivedPower"
    def setReceivedPower (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "receiverState"
    def getReceiverState (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "receiverState"
    def setReceiverState (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "transmitterSiteID"
    def getTransmitterSiteID (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "transmitterSiteID"
    def setTransmitterSiteID (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "transmitterApplicationID"
    def getTransmitterApplicationID (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "transmitterApplicationID"
    def setTransmitterApplicationID (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "transmitterEntityID"
    def getTransmitterEntityID (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "transmitterEntityID"
    def setTransmitterEntityID (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "transmitterRadioID"
    def getTransmitterRadioID (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "transmitterRadioID"
    def setTransmitterRadioID (self, value):
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
    def getGeoCoords (self, result):
        pass

    # Assign 3-tuple double array [] to SFVec3d inputOutput field named "geoCoords"
    def setGeoCoords (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return boolean result from SFBool outputOnly field named "isActive"
    def getIsActive (self):
        pass

    # Return boolean result from SFBool inputOutput field named "enabled"
    def getEnabled (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "enabled"
    def setEnabled (self, value):
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
