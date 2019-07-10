from . import *

# IndexedLineSet defines a concrete node interface that extends interface X3DGeometryNode.
class CIndexedLineSet(CX3DGeometryNode):
    m_strNodeName = "IndexedLineSet"
    def __init__(self):
        self.m_strNodeName = "IndexedLineSet"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0
 
    # Assign MFInt32 value using RGB values [0..1] to MFInt32 inputOnly field named "set_colorIndex"
    def setColorIndex1 (self, colors):
        pass

    # Assign single SFInt32 value using RGB values [0..1] as the MFInt32 array for inputOnly field named "set_colorIndex"
    def setColorIndex2 (self, color):
        pass

    # Assign MFInt32 value [] to MFInt32 inputOnly field named "set_coordIndex"
    def setCoordIndex1 (self, values, size):
        pass

    # Assign single SFInt32 value [] as the MFInt32 array for inputOnly field named "set_coordIndex"
    def setCoordIndex2 (self, value):
        pass

    # Return boolean result from SFBool initializeOnly field named "colorPerVertex"
    def getColorPerVertex (self):
        pass

    # Assign boolean value to SFBool initializeOnly field named "colorPerVertex"
    def setColorPerVertex (self, color):
        pass

    # Return MFInt32 result using RGB values [0..1] from MFInt32 initializeOnly field named "colorIndex"
    def getColorIndex (self):
        pass

    # Return number of primitive values in "colorIndex" array
    def getNumColorIndex (self):
        pass

    # Assign MFInt32 value using RGB values [0..1] to MFInt32 initializeOnly field named "colorIndex"
    def setColorIndex1 (self, colors, size):
        pass

    # Assign single SFInt32 value using RGB values [0..1] as the MFInt32 array for initializeOnly field named "colorIndex"
    def setColorIndex2 (self, color):
        pass

    # Return MFInt32 result [] from MFInt32 initializeOnly field named "coordIndex"
    def getCoordIndex (self):
        pass

    # Return number of primitive values in "coordIndex" array
    def getNumCoordIndex (self):
        pass

    # Assign MFInt32 value [] to MFInt32 initializeOnly field named "coordIndex"
    def setCoordIndex1 (self, values, size):
        pass

    # Assign single SFInt32 value [] as the MFInt32 array for initializeOnly field named "coordIndex"
    def setCoordIndex2 (self, value):
        pass

    # Return array of X3DVertexAttributeNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode inputOutput field named "attrib"
    def getAttrib (self, result):
        pass

    # Return number of nodes in "attrib" array
    def getNumAttrib (self):
        pass

    # Assign X3DVertexAttributeNode array (using a properly typed node array) to MFNode inputOutput field named "attrib"
    def setAttrib1 (self, nodes):
        pass

    # Assign single X3DVertexAttributeNode value (using a properly typed node) as the MFNode array for inputOutput field named "attrib"
    def setAttrib2 (self, node):
        pass

    # Assign X3DVertexAttributeNode array (using a properly typed protoInstance array) to MFNode inputOutput field named "attrib"
    def setAttrib3 (self, node):
        pass

    # Assign X3DVertexAttributeNode array (using a properly typed node array) to MFNode inputOutput field named "attrib"
    def setAttrib4 (self, nodes):
        pass

    # Return X3DColorNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "color"
    def getColor (self, result):
        pass

    # Assign X3DColorNode value (using a properly typed node) to SFNode inputOutput field named "color"
    def setColor1 (self, color):
        pass

    # Assign X3DColorNode value (using a properly typed protoInstance)
    def setColor2 (self, protoInstance):
        pass

    # Return X3DCoordinateNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "coord"
    def getCoord (self, result):
        pass

    # Assign X3DCoordinateNode value (using a properly typed node) to SFNode inputOutput field named "coord"
    def setCoord1 (self, node):
        pass

    # Assign X3DCoordinateNode value (using a properly typed protoInstance)
    def setCoord2 (self, protoInstance):
        pass

    # Return FogCoordinate result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "fogCoord"
    def getFogCoord (self, result):
        pass

    # Assign FogCoordinate value (using a properly typed node) to SFNode inputOutput field named "fogCoord"
    def setFogCoord1 (self, node):
        pass

    # Assign FogCoordinate value (using a properly typed protoInstance)
    def setFogCoord2 (self, protoInstance):
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