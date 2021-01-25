import sys
sys.path.insert(1, '..')
from vector import Vector
from sphere import Sphere
from ray import Ray
from math import sqrt, pi
from transforms import *

print("=====================================================")
print("The normal on a sphere at a point on the x axis")
s = Sphere()
n = s.getNormal(Vector(1, 0, 0, 1))
print("Normal = " + str(n))

print("The normal on a sphere at a point on the x axis")
s = Sphere()
n = s.getNormal(Vector(0, 1, 0, 1))
print("Normal = " + str(n))

print("The normal on a sphere at a point on the x axis")
s = Sphere()
n = s.getNormal(Vector(0, 0, 1, 1))
print("Normal = " + str(n))

print("The normal on a sphere at a point on the x axis")
s = Sphere()
n = s.getNormal(Vector(sqrt(3)/3, sqrt(3)/3, sqrt(3)/3, 1))
print("Normal = " + str(n))
nn = n.normalize()
print(n == nn)

print("Normal on a translated sphere")
s = Sphere()
s.setTransform(translation(0, 1, 0))
n = s.getNormal(Vector(0, 1.70711, -0.70711, 1))
print(n)

print("Normal on a transformed sphere")
s = Sphere()
M = scaling(1, 0.5, 1) * rotateZ(pi/5)
s.setTransform(M)
n = s.getNormal(Vector(0, sqrt(2)/2, -sqrt(2)/2, 1))
print(n)


print("\n\n\nReflecting")
print("Reflect vector at 45 degrees")
v = Vector(1, -1, 0)
n = Vector(0, 1, 0)
r = v.reflect(n)
print(r)

print("Reflect vector off slanted surface")
v = Vector(0, -1, 0)
n = Vector(sqrt(2)/2, sqrt(2)/2, 0)
r = v.reflect(n)
print(r)


