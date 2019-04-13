from X3DLib import *

class CMField(CX3DField):

    def size(self, parameter_list):
        raise NotImplementedError

    def clear(self, parameter_list):
        raise NotImplementedError

    def remove(self, parameter_list):
        raise NotImplementedError