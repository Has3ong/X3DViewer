from . import *

# MFVec2d defines an abstract node interface.
# MFVec2d is an array of SFVec2d values. Array values are optionally separated by commas.
class CMFVec2d(CMField):

    m_Values =[]

    # Return array of 2-tuple double results array [] from type MFVec2d
    def getValue1(self, result):
        pass

    # Return array of 2-tuple double results array [] from type MFVec2d
    def getValue2(self, result):
        pass

    # Utility method to return single 2-tuple value from MFVec2d array
    def getValue3(self, index, result):
        value = CSFVec2d()
        value = self.m_Values[index]
        result[0] = value.x()
        result[1] = value.y()

    # Assign 2-tuple double array [] to type MFVec2d
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

    # Assign 2-tuple double array [] to type MFVec2d
    def setValue2 (self, values) :
        pass

    # Utility method to set a single 2-tuple value in MFVec2d array
    def setValue3(self, index, value):
        val = CSFVec2d()
        np.double(value)
        val.setValue2(value[0], value[1])
        
        self.m_Values.insert(index, val)

    # Utility method to append a single 2-tuple value to MFVec2d array
    def append(self, value):
        val = CSFVec2d()
        np.douvle(value)
        val.setValue2(value[0], value[1])

        self.m_Values.append(val)

    # Utility method to insert a single 2-tuple value in MFVec2d array
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