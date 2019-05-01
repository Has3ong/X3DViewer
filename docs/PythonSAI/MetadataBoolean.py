from . import *

class CMetadataBoolean(CX3DNode, CX3DMetadataObject):
    m_strNodeName = "MetaDataBoolean"
    def __init__(self):
        self.m_strNodeName = "MetadataBoolean"
        self.m_Parent = [None]
        self.children = []
        self.SourceNode = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1

    pass