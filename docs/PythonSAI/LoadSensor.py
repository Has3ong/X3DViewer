from . import *

# LoadSensor defines a concrete node interface that extends interface X3DNetworkSensorNode.
class CLoadSensor(CX3DNetworkSensorNode):
    m_strNodeName = "LoadSensor"
    def __init__(self):
        self.m_strNodeName = "LoadSensor"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

    # Return boolean result from SFBool outputOnly field named "isLoaded"
    def getIsLoaded (self):
        pass

    # Return double result in seconds from SFTime outputOnly field named "loadTime"
    def getLoadTime (self):
        pass

    # Return float result [] from SFFloat outputOnly field named "progress"
    def getProgress (self):
        pass

    # Return double result in seconds from  type inputOutput field named "timeOut"
    def getTimeOut (self):
        pass

    # Assign double value in seconds to  type inputOutput field named "timeOut"
    def setTimeOut (self, timestamp):
        pass

    # Return array of X3DUrlObject results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "watchList"
    def getWatchList (self, result):
        pass

    # Return number of nodes in "watchList" array
    def getNumWatchList (self):
        pass

    # Assign X3DUrlObject array (using a properly typed node array) to MFNode inputOutput field named "watchList"
    def setWatchList (self, nodes):
        pass

    # Assign single X3DUrlObject value (using a properly typed node) as the MFNode array for inputOutput field named "watchList"
    def setWatchList (self, node):
        pass

    # Assign X3DUrlObject array (using a properly typed protoInstance array) to MFNode inputOutput field named "watchList"
    def setWatchList (self, node):
        pass

    # Assign X3DUrlObject array (using a properly typed node array) to MFNode inputOutput field named "watchList"
    def setWatchList (self, nodes):
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