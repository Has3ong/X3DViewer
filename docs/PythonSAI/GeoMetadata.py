from . import *

# GeoMetadata defines a concrete node interface that extends interface X3DInfoNode.
class CGeoetadata(CX3DInfoNode):
    m_strNodeName = "GeoMetadata"
    def __init__(self):
       self.m_strNodeName = "GeoMetadata"
       self.m_Parent = [None]
       self.children = []
       self.DEF = ""
       self.USE = ""
       self.n_Count = -1
       self.depth = 0

    # Return array of String results array [] from MFString inputOutput field named "url"
    def getUrl (self):
        pass

    # Return number of primitive values in "url" array
    def getNumUrl (self):
        pass

    # Assign String array [] to MFString inputOutput field named "url"
    def setUrl1 (self, values, size):
        pass

    # Assign single String value [] as the MFString array for inputOutput field named "url"
    def setUrl2 (self, value):
        pass

    # Return array of String results array [] from MFString inputOutput field named "summary"
    def getSummary (self):
        pass

    # Return number of primitive values in "summary" array
    def getNumSummary (self):
        pass

    # Assign String array [] to MFString inputOutput field named "summary"
    def setSummary1 (self, values, size):
        pass

    # Assign single String value [] as the MFString array for inputOutput field named "summary"
    def setSummary2 (self, value):
        pass

    # Return array of X3DNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "data"
    def getData (self, result):
        pass

    # Return number of nodes in "data" array
    def getNumData (self):
        pass

    # Assign X3DNode array (using a properly typed node array) to MFNode inputOutput field named "data"
    def setData1 (self, nodes):
        pass

    # Assign single X3DNode value (using a properly typed node) as the MFNode array for inputOutput field named "data"
    def setData2 (self, node):
        pass

    # Assign X3DNode array (using a properly typed protoInstance array) to MFNode inputOutput field named "data"
    def setData3 (self, node):
        pass

    # Assign X3DNode array (using a properly typed node array) to MFNode inputOutput field named "data"
    def setData4 (self, nodes):
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
