from . import *

class CX3DField:

    def getDefinition(self):
        return self.fieldDefinition

    def addX3DEventListner(self, l):
        raise NotImplementedError

    def removeX3DEventListener(self, l):
        raise NotImplementedError

    def setUserData(self, data):
        raise NotImplementedError

    def getUserData(self):
        raise NotImplementedError

    def isReadable(self):
        bRet = False
        if self.fieldDefinition.fieldType in ["inputOnly", "inputoutput"]:
            bRet = True

        return bRet

    def isWriteable(self):
        bRet = False
        if self.fieldDefinition.fieldType in ["outputOnly", "inputoutput"]:
            bRet = True

        return bRet