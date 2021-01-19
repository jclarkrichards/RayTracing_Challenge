from vector import Vector

class Color(Vector):
    def __init__(self, r, g, b):
        Vector.__init__(self, r, g, b)
        self.red = r
        self.green = g
        self.blue = b

    def __str__(self):
        return "Color<"+str(self.red)+", "+str(self.green)+", "+str(self.blue)+">"

    def hadamard(self, other):
        return Color(self.red*other.red, self.green*other.green, self.blue*other.blue)

    def asTuple(self):
        return (self.red, self.green, self.blue)

    def color255(self):
        return (self.red*255, self.green*255, self.blue*255)
