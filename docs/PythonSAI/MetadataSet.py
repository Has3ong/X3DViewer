from . import *

class CMetadataSet(CX3DNode, CX3DMetadataObject):
    m_strNodeName = "MetaDataSet"
    def __init__(self):
        self.m_strNodeName = "MetadataSet"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1


    pass