from . import *

# Fog defines a concrete node interface that extends interfaces X3DBindableNodeX3DFogObject.
class CFog(CX3DBindableNode):
    m_strNodeName = "Fog"
    def __init__(self):
        self.m_strNodeName = "Fog"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

    # Return array of 3-tuple float results array using RGB values [0..1] from SFColor inputOutput field named "color"
    def getColor (self):
        pass

    # Assign 3-tuple float array using RGB values [0..1] to SFColor inputOutput field named "color"
    def setColor (self, color):
        pass

    # Return String enumeration result ("LINEAR"|"EXPONENTIAL") from fogTypeValues type inputOutput field named "fogType"
    def getFogType (self):
        pass

    # Assign String enumeration value ("LINEAR"|"EXPONENTIAL") to fogTypeValues type inputOutput field named "fogType"
    def setFogType (self, value):
        pass

    # Return float result [] from  type inputOutput field named "visibilityRange"
    def getVisibilityRange (self):
        pass

    # Assign float value [] to  type inputOutput field named "visibilityRange"
    def setVisibilityRange (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Assign boolean value to SFBool inputOnly field named "set_bind"
    def setBind (self, value):
        pass

    # Return double result in seconds from SFTime outputOnly field named "bindTime"
    def getBindTime (self):
        pass

    # Return boolean result from SFBool outputOnly field named "isBound"
    def getIsBound (self):
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
