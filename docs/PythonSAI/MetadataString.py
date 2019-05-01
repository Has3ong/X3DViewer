from . import *

class CMetadataString(CX3DNode, CX3DMetadataObject):
    m_strNodeName = "MetaDataString"
    def __init__(self):
        self.m_strNodeName = "MetadataString"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1


    pass