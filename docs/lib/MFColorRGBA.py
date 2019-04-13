from X3DLib import *

class CMFColorRGBA(CMField):

    m_Values =[]
    
    def getValue1(self, result):
        return 0

    def getValue2(self, index, reslut):
        value = CSFColorRGBA()
        value = self.m_Values[index]
        result[0] = value.r()
        result[1] = value.g()
        result[2] = value.b()
        result[3] = value.a()

    def getValue3(self, index):
        return self.m_Values[index]

    def setValue1(self, size, color):
        r = 0.0
        g = 0.0
        b = 0.0
        a = 0.0

        for i in range(0, size):
            j = (i % 4)

            if j == 0 :
                r = colors[i]
                break
            elif j == 1:
                g = colors[i]
                break
            elif j == 2:
                b = colors[i]

            elif j == 3:
                a = colors[i]

                color = CSFColor()
                color.setValue2(r, g, b, a)

                self.m_Values.append(color)

                r = 0.0
                g = 0.0
                b = 0.0
                a = 0.0
                break
    
    def setValue2(self, index, color):
        value = CSFColorRGBA()
        value.setValue2(color[0], color[1], color[2], color[3])
        
        self.m_Values.insert(index, value)

    def append(self, color):
        value = CSFColorRGBA()
        value.setValue2(color[0], color[1], color[2], color[3])

        self.m_Values.append(value)

    def insertValue(self, index, color):
        value = CSFColorRGBA()
        value.setValue2(color[0], color[1], color[2], color[3])

        self.m_Values.insert(index, value)

    def size(self):
        return len(self.m_Values)
    
    def clear(self):
        self.m_Values.clear()

    def remove(self, index):
        del self.m_Values[index]