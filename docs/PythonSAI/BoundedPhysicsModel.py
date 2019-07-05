from . import *

# BoundedPhysicsModel defines a concrete node interface that extends interface X3DParticlePhysicsModelNode.
class CBoundedPhysicsModel(CX3DParticlePhysicsModelNode):
    m_strNodeName = "BoundedPhysicsModel"
    def __init__(self):
        self.m_strNodeName = "BoundedPhysicsModel"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return X3DGeometryNode result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "geometry"
    def getGeometry (self, result):
        pass

    # Assign X3DGeometryNode value (using a properly typed node) to SFNode inputOutput field named "geometry"
    def setGeometry1 (self, node):
        pass

    # Assign X3DGeometryNode value (using a properly typed protoInstance)
    def setGeometry2 (self, protoInstance):
        pass

    # ===== methods for fields inherited from parent interfaces =====

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