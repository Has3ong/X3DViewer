from X3DLib import *

class CMFBool(CMField):
    m_values = []

    def getValue1(self):
        return self.m_values
    
    def getValue2(self, index):
        bBool = self.m_values[index]
        return bBool

    def setValue1(self, size, values):
        for i in range (0, size):
            self.m_values.append(values)

    def setValue2(self, index, value):
        self.m_values.insert(index, value)

    def append(self, value):
        self.m_values.append(value)

    def insertValue(self, index, value):
        self.m_values.insert(index, value)

    def size(self):
        return len(self.m_values)

    def clear(self):
        self.m_values.clear()

    def remove(self, index):
        del self.m_values[index]