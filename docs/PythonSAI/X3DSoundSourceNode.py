from . import *

# X3DSoundSourceNode defines an abstract node interface that extends interfaces X3DChildNode, X3DNode.
# Nodes implementing X3DSoundSourceNode are allowed as children of Sound node.
class CX3DSoundSourceNode(CX3DTimeDependentNode):
    m_strNodeName = "X3DSoundSourceNode"
    def __init__(self):
        self.m_strNodeName = "X3DSoundSourceNode"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return double result in seconds from SFTime outputOnly field named "duration_changed"
    def getDuration (self):
        pass

    # Return String result [] from SFString inputOutput field named "description"
    def getDescription (self):
        pass

    # Assign String value [] to SFString inputOutput field named "description"
    def setDescription (self, value):
        pass

    # Return float result [] from  type inputOutput field named "pitch"
    def getPitch (self):
        pass

    # Assign float value [] to  type inputOutput field named "pitch"
    def setPitch (self, value) :
        pass

    # Return bool result from SFBool inputOutput field named "loop"
    def getLoop1 (self):
        pass

    # Assign bool value to SFBool inputOutput field named "loop"
    def setLoop1 (self, value):
        pass

    # Return double result in seconds from SFTime inputOutput field named "pauseTime"
    def getPauseTime1 (self):
        pass

    # Assign double value in seconds to SFTime inputOutput field named "pauseTime"
    def setPauseTime1 (self, timestamp) :
        pass

    # Return double result in seconds from SFTime inputOutput field named "resumeTime"
    def getResumeTime1 (self):
        pass

    # Assign double value in seconds to SFTime inputOutput field named "resumeTime"
    def setResumeTime1 (self, timestamp) :
        pass

    # Return double result in seconds from SFTime inputOutput field named "startTime"
    def getStartTime1 (self):
        pass

    # Assign double value in seconds to SFTime inputOutput field named "startTime"
    def setStartTime1 (self, timestamp) :
        pass

    # Return double result in seconds from SFTime inputOutput field named "stopTime"
    def getStopTime1 (self):
        pass

    # Assign double value in seconds to SFTime inputOutput field named "stopTime"
    def setStopTime1 (self, timestamp) :
        pass

    # ===== methods for fields inherited from parent interfaces =====

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
    def getLoop2 (self):
        pass

    # Assign bool value to SFBool inputOutput field named "loop"
    def setLoop2 (self, value):
        pass

    # Return double result in seconds from SFTime inputOutput field named "pauseTime"
    def getPauseTime2 (self):
        pass

    # Assign double value in seconds to SFTime inputOutput field named "pauseTime"
    def setPauseTime2 (self, timestamp) :
        pass

    # Return double result in seconds from SFTime inputOutput field named "resumeTime"
    def getResumeTime2 (self):
        pass

    # Assign double value in seconds to SFTime inputOutput field named "resumeTime"
    def setResumeTime2 (self, timestamp) :
        pass

    # Return double result in seconds from SFTime inputOutput field named "startTime"
    def getStartTime2 (self):
        pass

    # Assign double value in seconds to SFTime inputOutput field named "startTime"
    def setStartTime2 (self, timestamp) :
        pass

    # Return double result in seconds from SFTime inputOutput field named "stopTime"
    def getStopTime2 (self):
        pass

    # Assign double value in seconds to SFTime inputOutput field named "stopTime"
    def setStopTime2 (self, timestamp) :
        pass

    # Return X3DMetadataObject result (using a properly typed node or X3DPrototypeInstance) from SFNode inputOutput field named "metadata"
    def getMetadata(self):
        pass

    # Assign X3DMetadataObject value (using a properly typed node) to SFNode inputOutput field named "metadata"
    def setMetadata1 (self, node):
        pass

    # Assign X3DMetadataObject value (using a properly typed protoInstance)
    def setMetadata2 (self, protoInstance):
        pass