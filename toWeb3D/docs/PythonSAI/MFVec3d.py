from . import *

# MFVec3d defines an abstract node interface.
# MFVec3d is an array of SFVec3d values. Array values are optionally separated by commas. See GeoVRML 1.0 Recommended Practice, Section 2.3, Limitations of Single Precision. Hint: MFVec3d can be used to specify a list of georeferenced 3D coordinates.

class CMFVec3d(CMField):

    m_Values =[]

    # Return array of 3-tuple double results array [] from type MFVec3d
    def getValue1(self, result):
        pass

    # Return array of 3-tuple double results array [] from type MFVec3d
    def getValue2(self, result):
        pass

    # Utility method to return single 3-tuple value from MFVec3d array
    def getValue3(self, index, result):
        value = CSFVec3d()
        value = self.m_Values[index]
        result[0] = value.x()
        result[1] = value.y()
        result[2] = value.z()

    def setValue1(self, size, value):
        x = 0.0
        y = 0.0
        z = 0.0

        for i in range(0, size):
            j = (i % 3)

            if j == 0 :
                x = np.double(value[i])
                break
            elif j == 1:
                y = np.double(value[i])
                break

            elif j == 2:
                z = np.double(value[i])
                val = CSFVec3d()
                val.setValue2(x, y, z)

                self.m_Values.append(val)

                x = 0.0
                y = 0.0
                z = 0.0
                break

    # Assign 3-tuple double array [] to type MFVec3d
    def setValue2 (self, values) :
        pass

    # Utility method to set a single 3-tuple value in MFVec3d array
    def setValue3(self, index, value):
        val = CSFVec3d()
        np.double(value)
        val.setValue2(value[0], value[1], value[2])
        
        self.m_Values.insert(index, val)

    # Utility method to append a single 3-tuple value to MFVec3d array
    def append(self, value):
        val = CSFVec3d()
        np.double(value)
        val.setValue2(value[0], value[1], value[2])

        self.m_Values.append(val)

    # Utility method to insert a single 3-tuple value in MFVec3d array
    def insertValue(self, index, value):
        val = CSFVec3d()
        np.double(value)
        val.setValue2(value[0], value[1], value[2])

        self.m_Values.insert(index, val)

    def size(self):
        return len(self.m_Values)
    
    def clear(self):
        self.m_Values.clear()

    def remove(self, index):
        del self.m_Values[index]