import sys
sys.path.insert(1, '..')
from vector import Vector
from sphere import Sphere
from ray import Ray
from math import sqrt, pi
from transforms import *
from color import Color
from light import PointLight
from material import Material

print("=====================================================")
print("Point Light")
intensity = Color(1, 1, 1)
position = Vector(0, 0, 0, 1)
light = PointLight(position, intensity)
print(light.position)
print(light.intensity)

s = Sphere()
print(s.material)
s.material.ambient = 1
print(s.material)

print("Lighting with the eye between the light and the surface")
eyev = Vector(0, 0, -1)
normalv = Vector(0, 0, -1)
position = Vector(0, 0, 0, 1)
light = PointLight(Vector(0, 0, -10, 1), Color(1, 1, 1))
m = Material()
result = light.lighting(m, position, eyev, normalv)
print(result)

print("Lighting with the eye between light and surface, eye offset 45 degrees")
eyev = Vector(0, sqrt(2)/2, -sqrt(2)/2)
normalv = Vector(0, 0, -1)
position = Vector(0, 0, 0, 1)
light = PointLight(Vector(0, 0, -10, 1), Color(1, 1, 1))
m = Material()
result = light.lighting(m, position, eyev, normalv)
print(result)

print("Lighting with eye opposite surface, light offset 45 degrees")
eyev = Vector(0, 0, -1)
normalv = Vector(0, 0, -1)
position = Vector(0, 0, 0, 1)
light = PointLight(Vector(0, 10, -10, 1), Color(1, 1, 1))
m = Material()
result = light.lighting(m, position, eyev, normalv)
print(result)

print("Lighting with the eye between the light and the surface")
eyev = Vector(0, -sqrt(2)/2, -sqrt(2)/2)
normalv = Vector(0, 0, -1)
position = Vector(0, 0, 0, 1)
light = PointLight(Vector(0, 10, -10, 1), Color(1, 1, 1))
m = Material()
result = light.lighting(m, position, eyev, normalv)
print(result)

print("Lighting with the eye between the light and the surface")
eyev = Vector(0, 0, -1)
normalv = Vector(0, 0, -1)
position = Vector(0, 0, 0, 1)
light = PointLight(Vector(0, 0, 10, 1), Color(1, 1, 1))
m = Material()
result = light.lighting(m, position, eyev, normalv)
print(result)


