from . import *

# meta defines a concrete node interface that extends interface SceneGraphStructureStatement.
class CMeta(CX3DNode):
    m_strNodeName = "Meta"
    content = ""
    name = ""
    def __init__(self):
        self.m_strNodeName = "Meta"
        self.m_Parent = [None]
        self.children = []
        self.SourceNode = []
        self.DEF = ""
        self.USE = ""
        self.n_Count = -1
        self.depth = 0

    # Return String result http://www.dublincore.org/documents/dcmi-terms/#terms-description from SFString inputOutput field named "name"
    def getName (self):
        return self.name

    # Assign String value http://www.dublincore.org/documents/dcmi-terms/#terms-description to SFString inputOutput field named "name"
    def setName(self, value):
        self.name = value

    # Return String result http://www.w3.org/TR/html4/struct/global.html#adef-content from SFString inputOutput field named "content"
    def getContent (self):
        return self.content

    # Assign String value http://www.w3.org/TR/html4/struct/global.html#adef-content to SFString inputOutput field named "content"
    def setContent (self, value):
        self.content = value

    # Return String result [] from metaDirectionValues type inputOutput field named "dir"
    def getDir (self):
        pass

    # Assign String value [] to metaDirectionValues type inputOutput field named "dir"
    def setDir (self, value):
        pass

    # Return String result http://www.w3.org/TR/html4/struct/global.html#adef-http-equiv from SFString inputOutput field named "http-equiv"
    def getHttp_equiv (self):
        pass

    # Assign String value http://www.w3.org/TR/html4/struct/global.html#adef-http-equiv to SFString inputOutput field named "http-equiv"
    def setHttp_equiv (self, value):
        pass

    # Return String result http://www.w3.org/TR/html4/struct/dirlang.html#h-8.1.1 from SFString inputOutput field named "lang"
    def getLang (self):
        pass

    # Assign String value http://www.w3.org/TR/html4/struct/dirlang.html#h-8.1.1 to SFString inputOutput field named "lang"
    def setLang (self, value):
        pass

    # Return String result http://www.w3.org/TR/html4/struct/global.html#idx-scheme from SFString inputOutput field named "scheme"
    def getScheme (self):
        pass

    # Assign String value http://www.w3.org/TR/html4/struct/global.html#idx-scheme to SFString inputOutput field named "scheme"
    def setScheme (self, value):
        pass

    def toX3DString(self):
        data = """%s content='%s' name='%s'""" % (
            self.m_strNodeName, self.content, self.name
        )
        print(data)
        return data
