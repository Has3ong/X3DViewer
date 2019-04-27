from . import *

class CMFVec4d(CMField):

    m_Values =[]
    
    def getValue1(self, result):
        return 0

    def getValue2(self, index, result):
        value = CMFVec4d()
        value = self.m_Values[index]
        result[0] = value.x()
        result[1] = value.y()
        result[2] = value.z()
        result[3] = value.w()

    def getValue3(self, index):
        return self.m_Values[index]

    def setValue1(self, size, value):
        x = 0.0
        y = 0.0
        z = 0.0
        w = 0.0

        for i in range(0, size):
            j = (i % 4)

            if j == 0 :
                x = np.double(value[i])
                break
            elif j == 1:
                y = np.double(value[i])
                break
            elif j == 2:
                z = np.double(value[i])

            elif j == 3:
                w = np.double(value[i])

                val = CMFVec4d()
                val.setValue2(x, y, z, w)

                self.m_Values.append(val)

                x = 0.0
                y = 0.0
                z = 0.0
                w = 0.0
                break
    
    def setValue2(self, index, value):
        val = CMFVec4d()
        np.double(value)
        val.setValue2(value[0], value[1], value[2], value[3])
        
        self.m_Values.insert(index, val)

    def append(self, value):
        val = CMFVec4d()
        np.double(value)
        val.setValue2(value[0], value[1], value[2], value[3])

        self.m_Values.append(val)

    def insertValue(self, index, value):
        val = CMFVec4d()
        np.double(value)
        val.setValue2(value[0], value[1], value[2], value[3])

        self.m_Values.insert(index, val)

    def size(self):
        return len(self.m_Values)
    
    def clear(self):
        self.m_Values.clear()

    def remove(self, index):
        del self.m_Values[index]