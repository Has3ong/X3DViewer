from . import *

# MFRotation defines an abstract node interface.
# MFRotation is an array of SFRotation values. Array values are optionally separated by commas.
class CMFRotation(CMField):

    m_Values =[]

    # Return array of 4-tuple float results array in radians from type MFRotation
    def getValue1(self, result):
        pass

    # Return array of 4-tuple float results array in radians from type MFRotation
    def getValue2(self, index, result):
        value = CSFRotation()
        value = self.m_Values[index]
        result[0] = value.x()
        result[1] = value.y()
        result[2] = value.z()
        result[3] = value.rot()

    # Utility method to return single 4-tuple value from MFRotation array
    def getValue3(self, index):
        return self.m_Values[index]

    # Assign 4-tuple float array in radians to type MFRotation
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

    # Assign 4-tuple float array in radians to type MFRotation
    def setValue2(self, angles):
        pass

    # Utility method to set a single 4-tuple value in MFRotation array
    def setValue3(self, index, angle):
        value = CSFRotation()
        value.setValue2(angle[0], angle[1], angle[2], angle[3])
        
        self.m_Values.insert(index, value)

    # Utility method to append a single 4-tuple value to MFRotation array
    def append(self, angle):
        value = CSFRotation()
        value.setValue2(angle[0], angle[1], angle[2], angle[3])

        self.m_Values.append(value)

    # Utility method to insert a single 4-tuple value in MFRotation array
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