from . import *

# MFColor defines an abstract node interface.
# Array values are optionally separated by commas.
class CMFColor(CMField):

    m_Values = []

    # Return array of 3-tuple float results array using RGB values [0..1] from type MFColor
    def getValue1(self, result):
        pass

    # Return array of 3-tuple float results array using RGB values [0..1] from type MFColor
    def getValue2(self, index, result):
        value = CSFColor()
        value = self.m_Values[index]
        result[0] = value.r()
        result[1] = value.g()
        result[2] = value.b()

    # Utility method to return single 3-tuple value from MFColor array
    def getValue3(self, index):
        return self.m_Values[index]

    # Assign 3-tuple float array using RGB values [0..1] to type MFColor
    def setValue1(self, size, colors):
        r = 0.0
        g = 0.0
        b = 0.0

        for i in range(0, size):
            j = (i % 3)

            if j == 0 :
                r = colors[i]
                break
            elif j == 1:
                g = colors[i]
                break
            elif j == 2:
                b = colors[i]

                color = CSFColor()
                color.setValue2(r, g, b)

                self.m_Values.append(color)

                r = 0.0
                g = 0.0
                b = 0.0
                break

    # Assign 3-tuple float array using RGB values [0..1] to type MFColor
    def setValue2(selfself, colors):
        pass

    # Utility method to set a single 3-tuple value in MFColor array
    def setValue3(self, index, color):
        value = CSFColor()
        value.setValue2(color[0], color[1], color[2])

        self.m_Values.insert(index, value)

    # Utility method to append a single 3-tuple value to MFColor array
    def append(self, color):
        value = CSFColor()
        value.setValue2(color[0], color[1], color[2])

        self.m_Values.append(value)

    # Utility method to insert a single 3-tuple value in MFColor array
    def insertValue(self, index, color):
        value = CSFColor()
        value.setValue2(color[0], color[1], color[2])

        self.m_Values.insert(index, value)

    def size(self):
        return len(self.m_Values)

    def clear(self):
        self.m_Values.clear()

    def remove(self, index):
        del self.m_Values[index]