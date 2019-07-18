from . import *

# MFVec2f defines an abstract node interface.
# MFVec2f is an array of SFVec2f values. Array values are optionally separated by commas.
class CMFVec2f(CMField):

    m_Values =[]

    # Return array of 2-tuple float results array [] from type MFVec2f
    def getValue1(self, result):
        pass

    # Return array of 2-tuple float results array [] from type MFVec2f
    def getValue2(self, result):
        pass

    # Utility method to return single 2-tuple value from MFVec2f array
    def getValue3(self, index, result):
        value = CSFVec2f()
        value = self.m_Values[index]
        result[0] = value.x()
        result[1] = value.y()

    # Assign 2-tuple float array [] to type MFVec2f
    def setValue1(self, size, value):
        x = 0.0
        y = 0.0

        for i in range(0, size):
            j = (i % 2)

            if j == 0 :
                x = value[i]
                break
            elif j == 1:
                y = value[i]
                break

                val = CSFVec2f()
                val.setValue2(x, y)

                self.m_Values.append(val)

                x = 0.0
                y = 0.0
                break

    # Assign 2-tuple float array [] to type MFVec2f
    def setValue2 (self, values) :
        pass

    # Utility method to set a single 2-tuple value in MFVec2f array
    def setValue3(self, index, value):
        val = CSFVec2f()
        val.setValue2(value[0], value[1])
        
        self.m_Values.insert(index, val)

    # Utility method to append a single 2-tuple value to MFVec2f array
    def append(self, value):
        val = CSFVec2f()
        val.setValue2(value[0], value[1])

        self.m_Values.append(val)

    # Utility method to insert a single 2-tuple value in MFVec2f array
    def insertValue(self, index, value):
        val = CSFVec2f()
        val.setValue2(value[0], value[1])

        self.m_Values.insert(index, val)

    def size(self):
        return len(self.m_Values)
    
    def clear(self):
        self.m_Values.clear()

    def remove(self, index):
        del self.m_Values[index]