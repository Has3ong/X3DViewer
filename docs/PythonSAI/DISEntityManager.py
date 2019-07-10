from . import *

# DISEntityManager defines a concrete node interface that extends interface X3DChildNode.
class CDISEntityManager(CX3DChildNode):
    m_strNodeName = "DISEntityManager"
    def __init__(self):
        self.m_strNodeName = "DISEntityManager"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return String result [] from SFString inputOutput field named "address"
    def getAddress (self):
        pass

    # Assign String value [] to SFString inputOutput field named "address"
    def setAddress (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "applicationID"
    def getApplicationID (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "applicationID"
    def setApplicationID (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "port"
    def getPort (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "port"
    def setPort (self, value):
        pass

    # Return int result [] from SFInt32 inputOutput field named "siteID"
    def getSiteID (self):
        pass

    # Assign int value [] to SFInt32 inputOutput field named "siteID"
    def setSiteID (self, value):
        pass

    # Return array of EspduTransform results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode outputOnly field named "addedEntities"
    def getAddedEntities (self, result):
        pass

    # Return number of nodes in "addedEntities" array
    def getNumAddedEntities (self):
        pass

    # Return array of EspduTransform results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode outputOnly field named "removedEntities"
    def getRemovedEntities (self, result):
        pass

    # Return number of nodes in "removedEntities" array
    def getNumRemovedEntities (self):
        pass

    # Return array of DISEntityTypeMapping results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "mapping"
    def getMapping (self, result):
        pass

    # Return number of nodes in "mapping" array
    def getNumMapping (self):
        pass

    # Assign DISEntityTypeMapping array (using a properly typed node array) to MFNode inputOutput field named "mapping"
    def setMapping (self, nodes):
        pass

    # Assign single DISEntityTypeMapping value (using a properly typed node) as the MFNode array for inputOutput field named "mapping"
    def setMapping (self, node):
        pass

    # Assign DISEntityTypeMapping array (using a properly typed protoInstance array) to MFNode inputOutput field named "mapping"
    def setMapping (self, node):
        pass

    # Assign DISEntityTypeMapping array (using a properly typed node array) to MFNode inputOutput field named "mapping"
    def setMapping (self, nodes):
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
