from X3DLib import *

class CX3DField:
    fieldDefinition = CX3DFieldDefinition()

    def __init__(self):
        self.fieldDefinition = CX3DFieldDefinition()

    def getDefinition(self):
        return self.fieldDefinition

    def addX3DEventListner(self, l):
        return 0

    def removeX3DEventListener(self, l):
        return 0

    def setUserData(self, data):
        return 0

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