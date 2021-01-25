import math

'''
A Vector always has w=0
A Point always has w=1
'''
class Vector(object):
    def __init__(self, x, y, z, w=0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.epsilon = 0.00001
        
    def __str__(self):
        if self.w == 0:
            return "Vector<"+str(self.x)+", "+str(self.y)+", "+str(self.z)+">"
        else:
            return "Point<"+str(self.x)+", "+str(self.y)+", "+str(self.z)+">"

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y, self.z+other.z, self.w+other.w)

    def __sub__(self, other):
        return Vector(self.x-other.x, self.y-other.y, self.z-other.z, self.w-other.w)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z, -self.w)

    def __mul__(self, t):
        return Vector(self.x*t, self.y*t, self.z*t, self.w*t)

    def __div__(self, t):
        if t != 0:
            return Vector(self.x/float(t), self.y/float(t), self.z/float(t), self.w/float(t))
        return None

    def __truediv__(self, t):
        return self.__div__(t)

    def __eq__(self, other):
        if abs(self.x - other.x) < self.epsilon:
            if abs(self.y - other.y) < self.epsilon:
                if abs(self.z - other.z) < self.epsilon:
                    if abs(self.w - other.w) < self.epsilon:
                        return True
        return False

    def __hash__(self):
        return id(self)

    def magnitudeSquared(self):
        return self.x**2 + self.y**2 + self.z**2 + self.w**2

    def magnitude(self):
        return math.sqrt(self.magnitudeSquared())

    def normalize(self):
        mag = self.magnitude()
        if mag != 0:
            return self / mag
        return None

    def dot(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z + self.w*other.w

    def cross(self, other):
        return Vector(self.y*other.z - self.z*other.y,
                      self.z*other.x - self.x*other.z,
                      self.x*other.y - self.y*other.x,
                      self.w)

    def asTuple(self):
        return (self.x, self.y, self.z, self.w)
    
    def reflect(self, normal):
        '''Reflect this vector about a normal'''
        return self - normal * 2 * self.dot(normal)


