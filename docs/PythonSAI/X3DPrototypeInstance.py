from . import *

# X3DPrototypeInstance defines an abstract node interface.
# Note that direct children nodes are disallowed, let fieldValue with type SFNode/MFNode contain them.
class CX3DPrototypeInstance(CX3DNode):
    m_strNodeName = "X3DPrototypeInstance"
    def __init__(self):
        self.m_strNodeName = "X3DPrototypeInstance"
        self.m_Parent = [None]
        self.children = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth =0
    pass