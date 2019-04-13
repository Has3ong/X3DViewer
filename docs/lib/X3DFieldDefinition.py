from X3DLib import *

class CX3DFieldDefinition():

    name = ""
    accessType = 0
    fieldType = 0
    fieldTypeString = ""

    def __init__(self):
        self.name = ""
        self.accessType = 0
        self.fieldType = 0
        self.fieldTypeString = ""

    def setName(self, value):
        self.name = value

    def getName(self):
        return self.name

    def setAccessType(self, value):
        self.accessType = value

    def getAccessType(self):
        return self.accessType

    def setFieldType(self, value):
        self.fieldType = value

    def getFieldType(self):
        return self.fieldType

    def setFieldTypeString(self, value):
        self.fieldTypeString = value

    def getFieldTypeString(self):
        return self.fieldTypeString
    