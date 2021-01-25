from color import Color

class Material(object):
    def __init__(self):
        self.color = Color(1, 1, 1)
        self.ambient = 0.1
        self.diffuse = 0.9
        self.specular = 0.9
        self.shininess = 200.0

    def __str__(self):
        return "\nMaterial----\nColor: " + str(self.color) + "\nAmbient: " + str(self.ambient) + "\nDiffuse: " + str(self.diffuse) + "\nSpecular: " + str(self.specular) + "\nShininess: " + str(self.shininess)
