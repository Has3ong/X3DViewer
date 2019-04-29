from . import *
class CMFVec2d(CMField):

    m_Values =[]

    def getValue1(self, result):
        return 0

    def getValue2(self, index, result):
        value = CSFVec2d()
        value = self.m_Values[index]
        result[0] = value.x()
        result[1] = value.y()

    def getValue3(self, index):
        return self.m_Values[index]

    def setValue1(self, size, value):
        x = 0.0
        y = 0.0

        for i in range(0, size):
            j = (i % 2)

            if j == 0 :
                x = np.double(value[i])
                break
            elif j == 1:
                y = np.double(value[i])
                break

                val = CSFVec2d()
                val.setValue2(x, y)

                self.m_Values.append(val)

                x = 0.0
                y = 0.0
                break
    
    def setValue2(self, index, value):
        val = CSFVec2d()
        np.double(value)
        val.setValue2(value[0], value[1])
        
        self.m_Values.insert(index, val)

    def append(self, value):
        val = CSFVec2d()
        np.douvle(value)
        val.setValue2(value[0], value[1])

        self.m_Values.append(val)

    def insertValue(self, index, value):
        val = CSFVec2d()
        np.douvle(value)
        val.setValue2(value[0], value[1])

        self.m_Values.insert(index, val)

    def size(self):
        return len(self.m_Values)
    
    def clear(self):
        self.m_Values.clear()

    def remove(self, index):
        del self.m_Values[index]