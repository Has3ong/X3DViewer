from . import *

# X3DTimeDependentNode defines an abstract node interface that extends interfaces X3DNode.
class CX3DTimeDependentNode(CX3DChildNode):
    m_strNodeName = "X3DTimeDependentNode"
    def __init__(self):
        self.m_strNodeName = "X3DTimeDependentNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return double result in seconds from SFTime outputOnly field named "elapsedTime"
    def getElapsedTime (self):
        pass

    # Return bool result from SFBool outputOnly field named "isActive"
    def getIsActive (self):
        pass

    # Return bool result from SFBool outputOnly field named "isPaused"
    def getIsPaused (self):
        pass

    # Return bool result from SFBool inputOutput field named "loop"
    def getLoop (self):
        pass

    # Assign bool value to SFBool inputOutput field named "loop"
    def setLoop (self, value):
        pass

    # Return double result in seconds from SFTime inputOutput field named "pauseTime"
    def getPauseTime (self):
        pass

    # Assign double value in seconds to SFTime inputOutput field named "pauseTime"
    def setPauseTime (self, timestamp) :
        pass

    # Return double result in seconds from SFTime inputOutput field named "resumeTime"
    def getResumeTime (self):
        pass

    # Assign double value in seconds to SFTime inputOutput field named "resumeTime"
    def setResumeTime (self, timestamp) :
        pass

    # Return double result in seconds from SFTime inputOutput field named "startTime"
    def getStartTime (self):
        pass

    # Assign double value in seconds to SFTime inputOutput field named "startTime"
    def setStartTime (self, timestamp) :
        pass

    # Return double result in seconds from SFTime inputOutput field named "stopTime"
    def getStopTime (self):
        pass

    # Assign double value in seconds to SFTime inputOutput field named "stopTime"
    def setStopTime (self, timestamp) :
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return X3DMetadataObject result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "metadata"
    def getMetadata(self):
        pass

    # Assign X3DMetadataObject value (using a properly typed node) to SFNode inputOutput field named "metadata"
    def setMetadata1 (self, node):
        pass

    # Assign X3DMetadataObject value (using a properly typed protoInstance)
    def setMetadata2 (self, protoInstance):
        pass