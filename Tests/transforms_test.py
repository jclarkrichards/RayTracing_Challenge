import sys
sys.path.insert(1, '..')
from transforms import *
from matrix import Matrix
from vector import Vector
from math import pi

print("=================TRANSLATIONS=====================")
print("==========Multiplying by a translation Matrix=================\n")
T = translation(5, -3, 2)
p = Vector(-3, 4, 5, 1)
print(T)
print(p)
print("T * p = " + str(T * p))

print("\n==========Multiplying by the inverse of a translation Matrix=================\n")
T = translation(5, -3, 2)
T = T.inverse()
p = Vector(-3, 4, 5, 1)
print(T)
print(p)
print("T * p = " + str(T * p))

print("\n==========Translation does not affect vectors where w=0=================\n")
T = translation(5, -3, 2)
v = Vector(-3, 4, 5)
print(T)
print(v)
print("T * v = " + str(T * v))


print("=================SCALING=====================")
print("==========A Scaling Matrix applied to a Point=================\n")
T = scaling(2, 3, 4)
p = Vector(-4, 6, 8, 1)
print(T)
print(p)
print("T * p = " + str(T * p))

print("\n==========A Scaling Matrix applied to a Vector=================\n")
T = scaling(2, 3, 4)
v = Vector(-4, 6, 8)
print(T)
print(v)
print("T * v = " + str(T * v))

print("\n==========Multiplying by the inverse of a Matrix=================\n")
T = scaling(2, 3, 4)
T = T.inverse()
v = Vector(-4, 6, 8)
print(T)
print(v)
print("T * v = " + str(T * v))

print("\n==========Reflection is scaling by a negative value=================\n")
T = scaling(-1, 1, 1)
p = Vector(2, 3, 4, 1)
print(T)
print(p)
print("T * p = " + str(T * p))


print("\n=========================ROTATIONS========================")
print("\n=========================Rotating a point around the x axis==========")
p = Vector(0, 1, 0, 1)
hq = rotateX(pi / 4)
fq = rotateX(pi / 2)
print("hq * p = " + str(hq * p))
print("fq * p = " + str(fq * p))

print("\n===========The inverse rotates in the opposite direction==========")
p = Vector(0, 1, 0, 1)
hq = rotateX(pi / 4)
hq = hq.inverse()
print("hq * p = " + str(hq * p))

print("\n=========================Rotating a point around the y axis==========")
p = Vector(0, 0, 1, 1)
hq = rotateY(pi / 4)
fq = rotateY(pi / 2)
print("hq * p = " + str(hq * p))
print("fq * p = " + str(fq * p))

print("\n===========The inverse rotates in the opposite direction==========")
p = Vector(0, 0, 1, 1)
hq = rotateY(pi / 4)
hq = hq.inverse()
print("hq * p = " + str(hq * p))

print("\n=========================Rotating a point around the z axis==========")
p = Vector(0, 1, 0, 1)
hq = rotateZ(pi / 4)
fq = rotateZ(pi / 2)
print("hq * p = " + str(hq * p))
print("fq * p = " + str(fq * p))

print("\n===========The inverse rotates in the opposite direction==========")
p = Vector(0, 1, 0, 1)
hq = rotateZ(pi / 4)
hq = hq.inverse()
print("hq * p = " + str(hq * p))


print("\n================SKEWING==========================")
print("\n===========Shearing moves x in proportion to y")
p = Vector(2, 3, 4, 1)
T = shearing(1, 0, 0, 0, 0, 0)
print(p)
print(T * p)

print("\n===========Shearing moves x in proportion to z")
p = Vector(2, 3, 4, 1)
T = shearing(0, 1, 0, 0, 0, 0)
print(p)
print(T * p)

print("\n===========Shearing moves y in proportion to x")
p = Vector(2, 3, 4, 1)
T = shearing(0, 0, 1, 0, 0, 0)
print(p)
print(T * p)

print("\n===========Shearing moves y in proportion to z")
p = Vector(2, 3, 4, 1)
T = shearing(0, 0, 0, 1, 0, 0)
print(p)
print(T * p)

print("\n===========Shearing moves z in proportion to x")
p = Vector(2, 3, 4, 1)
T = shearing(0, 0, 0, 0, 1, 0)
print(p)
print(T * p)

print("\n===========Shearing moves z in proportion to y")
p = Vector(2, 3, 4, 1)
T = shearing(0, 0, 0, 0, 0, 1)
print(p)
print(T * p)


print("==============COMBINING TRANSFORMATIONS================")
p = Vector(1, 0, 1, 1)
print(p)
A = rotateX(pi/2)
B = scaling(5,5,5)
C = translation(10, 5, 7)
print(C * B * A * p)





