from vector import Vector

'''
Make sure color is always between 0 and 1.  Clamp the values
'''
class Color(object):
    def __init__(self, r, g, b):
        #Vector.__init__(self, r, g, b)
        self.red = min(r, 1)
        self.green = min(g, 1)
        self.blue = min(b, 1)

    def __str__(self):
        return "Color<"+str(self.red)+", "+str(self.green)+", "+str(self.blue)+">"

    def hadamard(self, other):
        return Color(self.red*other.red, self.green*other.green, self.blue*other.blue)

    def asTuple(self):
        return (self.red, self.green, self.blue)

    def color255(self):
        return (self.red*255, self.green*255, self.blue*255)

    def __mul__(self, other):
        if type(other) == Color:
            return Color(self.red*other.red, self.green*other.green, self.blue*other.blue)
        else:
            #print(other)
            c = Color(self.red*other, self.green*other, self.blue*other)
            #if c.red < 0: c.red = 0
            #if c.green < 0: c.green = 0
            #if c.blue < 0: c.blue = 0
            #if c.red > 255: c.red = 255
            #if c.green > 255: c.green = 255
            #if c.blue > 255: c.blue = 255
            #print(c)
            return c
            
    def __add__(self, other):
        return Color(self.red + other.red, self.green+other.green, self.blue+other.blue)
