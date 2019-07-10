from . import *

# TimeSensor defines a concrete node interface that extends interfaces X3DTimeDependentNodeX3DSensorNode.
class CTimeSensor(CX3DTimeDependentNode, CX3DSensorNode):
    m_strNodeName = "TimeSensor"
    def __init__(self):
        self.m_strNodeName = "TimeSensor"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return double result in seconds from SFTime outputOnly field named "cycleTime"
    def getCycleTime (self):
        pass

    # Return float result [] from SFFloat outputOnly field named "fraction_changed"
    def getFraction (self):
        pass

    # Return double result in seconds from SFTime outputOnly field named "time"
    def getTime (self):
        pass

    # Return double result in seconds from  type inputOutput field named "cycleInterval"
    def getCycleInterval (self):
        pass

    # Assign double value in seconds to  type inputOutput field named "cycleInterval"
    def setCycleInterval (self, timestamp):
        pass

    # Return boolean result from SFBool inputOutput field named "enabled"
    def getEnabled (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "enabled"
    def setEnabled (self, value):
        pass

    # ===== methods for fields inherited from parent interfaces =====

    # Return double result in seconds from SFTime outputOnly field named "elapsedTime"
    def getElapsedTime (self):
        pass

    # Return boolean result from SFBool outputOnly field named "isActive"
    def getIsActive (self):
        pass

    # Return boolean result from SFBool outputOnly field named "isPaused"
    def getIsPaused (self):
        pass

    # Return boolean result from SFBool inputOutput field named "loop"
    def getLoop (self):
        pass

    # Assign boolean value to SFBool inputOutput field named "loop"
    def setLoop (self, value):
        pass

    # Return double result in seconds from SFTime inputOutput field named "pauseTime"
    def getPauseTime (self):
        pass

    # Assign double value in seconds to SFTime inputOutput field named "pauseTime"
    def setPauseTime (self, timestamp):
        pass

    # Return double result in seconds from SFTime inputOutput field named "resumeTime"
    def getResumeTime (self):
        pass

    # Assign double value in seconds to SFTime inputOutput field named "resumeTime"
    def setResumeTime (self, timestamp):
        pass

    # Return double result in seconds from SFTime inputOutput field named "startTime"
    def getStartTime (self):
        pass

    # Assign double value in seconds to SFTime inputOutput field named "startTime"
    def setStartTime (self, timestamp):
        pass

    # Return double result in seconds from SFTime inputOutput field named "stopTime"
    def getStopTime (self):
        pass

    # Assign double value in seconds to SFTime inputOutput field named "stopTime"
    def setStopTime (self, timestamp):
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
