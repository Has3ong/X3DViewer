from . import *

class CScene(CSceneGraphStructureStatement):

    m_strNodeName = "Scene"
    DEF = ""
    USE = ""

    def __init__(self):
        self.m_Parent = [None]
        self.children = []
