from X3DLib import *

class CMFInt32(CMField):

    m_Values = []

    def __init__(self):
        self.m_Values = []

    def getValue1(self):
        return self.m_Values

    def getValue2(self, index):
        return self.m_Values[index]

    def setValue1(self, size, values):
        for i in range (0, size):
            self.m_Values.append(np.int32(values[i]))
    
    def setValue2(self, index, value):
        self.m_Values.insert(index, np.int32(value))

    def append(self, value):
        self.m_Values.append(np.int32(value))

    def insertValue(self, index, value):
        self.m_Values.insert(index, np.int32(value))

    def size(self):
        return len(self.m_Values)
    
    def clear(self):
        self.m_Values.clear()

    def remove(self, index):
        del self.m_Values[index]