from . import *

# NavigationInfo defines a concrete node interface that extends interface X3DBindableNode.
class CNavigationInfo(CX3DBindableNode):
    m_strNodeName = "NavigationInfo"
    def __init__(self):
        self.m_strNodeName = "NavigationInfo"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return boolean result from SFBool outputOnly field named "transitionComplete"
    def getTransitionComplete (self):
        pass

    # Return array of float results array [] from MFFloat inputOutput field named "avatarSize"
    def getAvatarSize (self):
        pass

    # Return number of primitive values in "avatarSize" array
    def getNumAvatarSize (self):
        pass

    # Assign float array [] to MFFloat inputOutput field named "avatarSize"
    def setAvatarSize1 (self, values, size):
        pass

    # Assign single float value [] as the MFFloat array for inputOutput field named "avatarSize"
    def setAvatarSize2 (self, value):
        pass

    # Return boolean result from SFBool inputOutput field named "headlight"
    def getHeadlight (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "headlight"
    def setHeadlight (self, value):
        pass

    # Return float result [] from  type inputOutput field named "speed"
    def getSpeed (self):
        pass

    # Assign float value [] to  type inputOutput field named "speed"
    def setSpeed (self, value):
        pass

    # Return array of String results array ["ANY","WALK","EXAMINE","FLY","LOOKAT","NONE","EXPLORE",...] from MFString inputOutput field named "type"
    def getType (self):
        pass

    # Return number of primitive values in "type" array
    def getNumType (self):
        pass

    # Assign String array ["ANY","WALK","EXAMINE","FLY","LOOKAT","NONE","EXPLORE",...] to MFString inputOutput field named "type"
    def setType1 (self, values, size):
        pass

    # Assign single String value ["ANY","WALK","EXAMINE","FLY","LOOKAT","NONE","EXPLORE",...] as the MFString array for inputOutput field named "type"
    def setType2 (self, value):
        pass

    # Return array of String results array ["TELEPORT","LINEAR","ANIMATE",...] from MFString inputOutput field named "transitionType"
    def getTransitionType (self):
        pass

    # Return number of primitive values in "transitionType" array
    def getNumTransitionType (self):
        pass

    # Assign String array ["TELEPORT","LINEAR","ANIMATE",...] to MFString inputOutput field named "transitionType"
    def setTransitionType1 (self, values, size):
        pass

    # Assign single String value ["TELEPORT","LINEAR","ANIMATE",...] as the MFString array for inputOutput field named "transitionType"
    def setTransitionType2 (self, value):
        pass

    # Return double result in seconds from  type inputOutput field named "transitionTime"
    def getTransitionTime (self):
        pass

    # Assign double value in seconds to  type inputOutput field named "transitionTime"
    def setTransitionTime (self, timestamp):
        pass

    # Return float result [] from  type inputOutput field named "visibilityLimit"
    def getVisibilityLimit (self):
        pass

    # Assign float value [] to  type inputOutput field named "visibilityLimit"
    def setVisibilityLimit (self, value):
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
