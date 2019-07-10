from . import *

# MetadataSet defines a concrete node interface that extends interfaces X3DMetadataObject.
class CMetadataSet(CX3DNode, CX3DMetadataObject):
    m_strNodeName = "MetaDataSet"
    def __init__(self):
        self.m_strNodeName = "MetadataSet"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

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

    # Return array of X3DMetadataObject results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "value"
    def getValue (self, result):
        pass

    # Return number of nodes in "value" array
    def getNumValue (self):
        pass

    # Assign X3DMetadataObject array (using a properly typed node array) to MFNode inputOutput field named "value"
    def setValue1 (self, nodes):
        pass

    # Assign single X3DMetadataObject value (using a properly typed node) as the MFNode array for inputOutput field named "value"
    def setValue2 (self, node):
        pass

    # Assign X3DMetadataObject array (using a properly typed protoInstance array) to MFNode inputOutput field named "value"
    def setValue3 (self, node):
        pass

    # Assign X3DMetadataObject array (using a properly typed node array) to MFNode inputOutput field named "value"
    def setValue4 (self, nodes):
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
