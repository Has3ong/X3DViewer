from . import *

# MetadataBoolean defines a concrete node interface that extends interface X3DMetadataObject.
class CMetadataBoolean(CX3DNode, CX3DMetadataObject):
    m_strNodeName = "MetaDataBoolean"
    def __init__(self):
        self.m_strNodeName = "MetadataBoolean"
        self.m_Parent = [None]
        self.children = []
        self.SourceNode = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of boolean results array from MFBool inputOutput field named "value"
    def getValue (self):
        pass

    # Return number of primitive values in "value" array
    def getNumValue (self):
        pass

    # Assign boolean array to MFBool inputOutput field named "value"
    def setValue1 (self, values, size):
        pass

    # Assign single boolean value as the MFBool array for inputOutput field named "value"
    def setValu2e (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return String result [] from SFString inputOutput field named "name"
    def getName (self):
        pass

    # Assign String value [] to SFString inputOutput field named "name"
    def setName (self, value):
        pass

    # Return String result [] from SFString inputOutput field named "reference"
    def getReference (self):
        pass

    # Assign String value [] to SFString inputOutput field named "reference"
    def setReference (self, value):
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
