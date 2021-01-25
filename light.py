from color import Color
import math

class PointLight(object):
    def __init__(self, position, intensity):
        self.position = position
        self.intensity = intensity

    def lighting(self, material, point, eye, normal):
        #print(material.color)
        #print(self.intensity)
        effective_color = material.color * self.intensity
        temp = self.position - point
        lightv = temp.normalize()
        ambient = effective_color * material.ambient
        light_dot_normal = lightv.dot(normal)
        if light_dot_normal < 0:
            diffuse = Color(0, 0, 0)
            specular = Color(0, 0, 0)
        else:
            diffuse = effective_color * material.diffuse * light_dot_normal
            neg_lightv = lightv * -1
            reflectv = neg_lightv.reflect(normal)
            reflect_dot_eye = reflectv.dot(eye)

            if reflect_dot_eye <= 0:
                specular = Color(0, 0, 0)
            else:
                factor = math.pow(reflect_dot_eye, material.shininess)
                specular = self.intensity * material.specular * factor
        return ambient + diffuse + specular
