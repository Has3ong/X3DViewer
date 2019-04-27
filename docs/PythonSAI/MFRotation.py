from . import *

class CMFRotation(CMField):

    m_Values =[]

    def getValue1(self, result):
        return 0

    def getValue2(self, index, result):
        value = CSFRotation()
        value = self.m_Values[index]
        result[0] = value.x()
        result[1] = value.y()
        result[2] = value.z()
        result[3] = value.rot()

    def getValue3(self, index):
        return self.m_Values[index]

    def setValue1(self, size, angle):
        x = 0.0
        y = 0.0
        z = 0.0
        r = 0.0

        for i in range(0, size):
            j = (i % 4)

            if j == 0 :
                x = angle[i]
                break
            elif j == 1:
                y = angle[i]
                break
            elif j == 2:
                z = angle[i]

            elif j == 3:
                r = angle[i]

                rot = CSFRotation()
                rot.setValue2(x, y, z, r)

                self.m_Values.append(rot)

                x = 0.0
                y = 0.0
                z = 0.0
                r = 0.0
                break
    
    def setValue2(self, index, angle):
        value = CSFRotation()
        value.setValue2(angle[0], angle[1], angle[2], angle[3])
        
        self.m_Values.insert(index, value)

    def append(self, angle):
        value = CSFRotation()
        value.setValue2(angle[0], angle[1], angle[2], angle[3])

        self.m_Values.append(value)

    def insertValue(self, index, angle):
        value = CSFRotation()
        value.setValue2(angle[0], angle[1], angle[2], angle[3])

        self.m_Values.insert(index, value)

    def size(self):
        return len(self.m_Values)
    
    def clear(self):
        self.m_Values.clear()

    def remove(self, index):
        del self.m_Values[index]