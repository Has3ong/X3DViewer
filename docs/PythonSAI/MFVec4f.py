from . import *

# MFVec4f defines an abstract node interface.
# MFVec4f is zero or more SFVec4f values.
class CMFVec4f(CMField):

    m_Values =[]

    # Return array of 4-tuple float results array [] from type MFVec4f
    def getValue1(self, result):
        pass

    # Return array of 4-tuple float results array [] from type MFVec4f
    def getValue2(self, result):
        pass

    # Utility method to return single 4-tuple value from MFVec4f array
    def getValue3(self, index, result):
        value = CMFVec4f()
        value = self.m_Values[index]
        result[0] = value.x()
        result[1] = value.y()
        result[2] = value.z()
        result[3] = value.w()

    # Assign 4-tuple float array [] to type MFVec4f
    def setValue1(self, size, value):
        x = 0.0
        y = 0.0
        z = 0.0
        w = 0.0

        for i in range(0, size):
            j = (i % 4)

            if j == 0 :
                x = value[i]
                break
            elif j == 1:
                y = value[i]
                break
            elif j == 2:
                z = value[i]

            elif j == 3:
                w = value[i]

                val = CMFVec4f()
                val.setValue2(x, y, z, w)

                self.m_Values.append(val)

                x = 0.0
                y = 0.0
                z = 0.0
                w = 0.0
                break

    # Assign 4-tuple float array [] to type MFVec4f
    def setValue2 (self, values) :
        pass

    # Utility method to set a single 4-tuple value in MFVec4f array
    def setValue3(self, index, value):
        val = CMFVec4f()
        val.setValue2(value[0], value[1], value[2], value[3])
        
        self.m_Values.insert(index, val)

    # Utility method to append a single 4-tuple value to MFVec4f array
    def append(self, value):
        val = CMFVec4f()
        val.setValue2(value[0], value[1], value[2], value[3])

        self.m_Values.append(val)

    # Utility method to insert a single 4-tuple value in MFVec4f array
    def insertValue(self, index, value):
        val = CMFVec4f()
        val.setValue2(value[0], value[1], value[2], value[3])

        self.m_Values.insert(index, val)

    def size(self):
        return len(self.m_Values)
    
    def clear(self):
        self.m_Values.clear()

    def remove(self, index):
        del self.m_Values[index]