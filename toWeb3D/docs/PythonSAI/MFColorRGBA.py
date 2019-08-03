from . import *

# MFColorRGBA defines an abstract node interface.
class CMFColorRGBA(CMField):

    m_Values = []

    # Return array of 4-tuple float results array using RGBA values [0..1] from type MFColorRGBA
    def getValue1(self, result):
        return 0

    # Return array of 4-tuple float results array using RGBA values [0..1] from type MFColorRGBA
    def getValue2(self, index, reslut):
        value = CSFColorRGBA()
        value = self.m_Values[index]
        result[0] = value.r()
        result[1] = value.g()
        result[2] = value.b()
        result[3] = value.a()

    # Utility method to return single 4-tuple value from MFColorRGBA array
    def getValue3(self, index):
        return self.m_Values[index]

    # Assign 4-tuple float array using RGBA values [0..1] to type MFColorRGBA
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

    # Assign 4-tuple float array using RGBA values [0..1] to type MFColorRGBA
    def setValue2(self, colors):
        pass

    # Utility method to set a single 4-tuple value in MFColorRGBA array
    def setValue3(self, index, color):
        value = CSFColorRGBA()
        value.setValue2(color[0], color[1], color[2], color[3])
        
        self.m_Values.insert(index, value)

    # Utility method to append a single 4-tuple value to MFColorRGBA array
    def append(self, color):
        value = CSFColorRGBA()
        value.setValue2(color[0], color[1], color[2], color[3])

        self.m_Values.append(value)

    # Utility method to insert a single 4-tuple value in MFColorRGBA array
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