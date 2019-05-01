from . import *

class CFieldArray():
    m_values =[]
    def __init__(self):
        self.m_values = []

    def Add(self, value):
        self.m_values.append(value)

    def get(self, value):
        length = len(self.m_values)

        for i in range(0, length):
            if self.m_values[i].name == value:
                return self.m_values[i]


