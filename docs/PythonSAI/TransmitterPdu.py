from . import *

# TransmitterPdu defines a concrete node interface that extends interfaces X3DNetworkSensorNodeX3DBoundedObject.
class CTransmitterPdu(CX3DSensorNode):
    m_strNodeName = "TransmitterPdu"
    def __init__(self):
        self.m_strNodeName = "TransmitterPdu"
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

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "antennaLocation"
    def getAntennaLocation (self, result):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "antennaLocation"
    def setAntennaLocation (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "antennaPatternLength"
    def getAntennaPatternLength (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "antennaPatternLength"
    def setAntennaPatternLength (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "antennaPatternType"
    def getAntennaPatternType (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "antennaPatternType"
    def setAntennaPatternType (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "cryptoKeyID"
    def getCryptoKeyID (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "cryptoKeyID"
    def setCryptoKeyID (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "cryptoSystem"
    def getCryptoSystem (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "cryptoSystem"
    def setCryptoSystem (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "frequency"
    def getFrequency (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "frequency"
    def setFrequency (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "inputSource"
    def getInputSource (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "inputSource"
    def setInputSource (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "lengthOfModulationParameters"
    def getLengthOfModulationParameters (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "lengthOfModulationParameters"
    def setLengthOfModulationParameters (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "modulationTypeDetail"
    def getModulationTypeDetail (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "modulationTypeDetail"
    def setModulationTypeDetail (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "modulationTypeMajor"
    def getModulationTypeMajor (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "modulationTypeMajor"
    def setModulationTypeMajor (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "modulationTypeSpreadSpectrum"
    def getModulationTypeSpreadSpectrum (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "modulationTypeSpreadSpectrum"
    def setModulationTypeSpreadSpectrum (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "modulationTypeSystem"
    def getModulationTypeSystem (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "modulationTypeSystem"
    def setModulationTypeSystem (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "power"
    def getPower (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "power"
    def setPower (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "radioEntityTypeCategory"
    def getRadioEntityTypeCategory (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "radioEntityTypeCategory"
    def setRadioEntityTypeCategory (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "radioEntityTypeCountry"
    def getRadioEntityTypeCountry (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "radioEntityTypeCountry"
    def setRadioEntityTypeCountry (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "radioEntityTypeDomain"
    def getRadioEntityTypeDomain (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "radioEntityTypeDomain"
    def setRadioEntityTypeDomain (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "radioEntityTypeKind"
    def getRadioEntityTypeKind (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "radioEntityTypeKind"
    def setRadioEntityTypeKind (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "radioEntityTypeNomenclature"
    def getRadioEntityTypeNomenclature (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "radioEntityTypeNomenclature"
    def setRadioEntityTypeNomenclature (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "radioEntityTypeNomenclatureVersion"
    def getRadioEntityTypeNomenclatureVersion (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "radioEntityTypeNomenclatureVersion"
    def setRadioEntityTypeNomenclatureVersion (self, value):
        pass

    # Return array of 3-tuple float results array [] from SFVec3f inputOutput field named "relativeAntennaLocation"
    def getRelativeAntennaLocation (self, result):
        pass

    # Assign 3-tuple float array [] to SFVec3f inputOutput field named "relativeAntennaLocation"
    def setRelativeAntennaLocation (self, value):
        pass

    # Return float result [] from SFFloat inputOutput field named "transmitFrequencyBandwidth"
    def getTransmitFrequencyBandwidth (self):
        pass

    # Assign float value [] to SFFloat inputOutput field named "transmitFrequencyBandwidth"
    def setTransmitFrequencyBandwidth (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "transmitState"
    def getTransmitState (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "transmitState"
    def setTransmitState (self, value):
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
