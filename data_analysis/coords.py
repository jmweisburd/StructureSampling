import math
#Simple class for representing cartesian coordinates in 3D space
class CartesianCoords:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance(self, other):
        x_d = pow((self.x - other.x),2)
        y_d = pow((self.y - other.y),2)
        z_d = pow((self.z - other.z),2)
        return math.sqrt(x_d+y_d+z_d)

    def __repr__(self):
        return(str(self.x) + "," + str(self.y) + "," + str(self.z))

    def __lt__(self, other):
        if (self.x != other.x):
            return self.x < other.x
        if (self.y != other.y):
            return self.y < other.y
        return self.s < other.z

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __eq__(self, other):
        x_bool = (self.x == other.x)
        y_bool = (self.y == other.y)
        z_bool = (self.z == other.z)
        return (x_bool and y_bool and z_bool)
