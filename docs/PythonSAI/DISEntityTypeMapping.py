from . import *

# DISEntityTypeMapping defines a concrete node interface that extends interfaces X3DNodeX3DChildNode, X3DUrlObject.
class CDISEntityTypeMapping(CX3DInfoNode):
    m_strNodeName = "DISEntityTypeMapping"
    def __init__(self):
        self.m_strNodeName = "DISEntityTypeMapping"
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

    # Return int result [] from  type initializeOnly field named "category"
    def getCategory (self):
        pass

    # Assign int value [] to  type initializeOnly field named "category"
    def setCategory (self, value):
        pass

    # Return int result [] from  type initializeOnly field named "country"
    def getCountry (self):
        pass

    # Assign int value [] to  type initializeOnly field named "country"
    def setCountry (self, value):
        pass

    # Return int result [] from  type initializeOnly field named "domain"
    def getDomain (self):
        pass

    # Assign int value [] to  type initializeOnly field named "domain"
    def setDomain (self, value):
        pass

    # Return int result [] from  type initializeOnly field named "extra"
    def getExtra (self):
        pass

    # Assign int value [] to  type initializeOnly field named "extra"
    def setExtra (self, value):
        pass

    # Return int result [] from  type initializeOnly field named "kind"
    def getKind (self):
        pass

    # Assign int value [] to  type initializeOnly field named "kind"
    def setKind (self, value):
        pass

    # Return int result [] from  type initializeOnly field named "specific"
    def getSpecific (self):
        pass

    # Assign int value [] to  type initializeOnly field named "specific"
    def setSpecific (self, value):
        pass

    # Return int result [] from  type initializeOnly field named "subcategory"
    def getSubcategory (self):
        pass

    # Assign int value [] to  type initializeOnly field named "subcategory"
    def setSubcategory (self, value):
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
