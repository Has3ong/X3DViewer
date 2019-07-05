from . import *

# CollisionSensor defines a concrete node interface that extends interface X3DSensorNode.
class CCollisionSensor(CX3DSensorNode):
    m_strNodeName = "CollisionSensor"
    def __init__(self):
        self.m_strNodeName = "CollisionSensor"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return array of X3DNBodyCollidableNode results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode outputOnly field named "intersections"
    def getIntersections (self, result):
        pass

    # Return number of nodes in "intersections" array
    def getNumIntersections (self):
        pass

    # Return array of Contact results array (using a properly typed node array or X3DPrototypeInstance array) from MFNode outputOnly field named "contacts"
    def getContacts (self, result):
        pass

    # Return number of nodes in "contacts" array
    def getNumContacts (self):
        pass

    # Return CollisionCollection result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "collider"
    def getCollider (self, result):
        pass

    # Assign CollisionCollection value (using a properly typed node) to SFNode inputOutput field named "collider"
    def setCollider1 (self, node):
        pass

    # Assign CollisionCollection value (using a properly typed protoInstance)
    def setCollider2 (self, protoInstance):
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