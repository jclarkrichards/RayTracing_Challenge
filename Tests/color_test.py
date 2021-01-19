import sys
sys.path.insert(1, '..')
#sys.path.insert(1, 'C:\\Users\\admin\\Documents\\RayTracing_Challenge')
from color import Color

print("=====================================================")
print("Color")
p = Color(-.5, .4, 1.7)
print(p)



print("==========================Adding=========================")
print("Color + Color = Color")
a1 = Color(.9, .6, .75)
a2 = Color(.7, .1, .25)
print(str(a1) + " + " + str(a2) +" = " + str(a1 + a2))
print("=====================================================\n\n")

print("=======================Subtract==========================")
print("Point - Point = Vector")
a1 = Color(.9, .6, .75)
a2 = Color(.7, .1, .25)
print(str(a1) + " - " + str(a2) +" = " + str(a1 - a2))
print("=====================================================\n\n")

print("=======================Multiply by Scalar==========================")
print("Point - Point = Vector")
a1 = Color(.2, .3, .4)
s = 2
print(str(a1) + " * 2 = " + str(a1 * 2))
print("=====================================================\n\n")

print("=======================Multiply by Color==========================")
print("Point - Point = Vector")
a1 = Color(1, .2, .4)
a2 = Color(.9, 1, .1)
print(str(a1) + " * " + str(a2) + " = " + str(a1.hadamard(a2)))
print("=====================================================\n\n")


"""
print("==========================Negating=========================")
print("Point => -Point")
a1 = Point(3, -2, 5)
print(str(a1) + " => " + str(-a1))
print("=====================================================\n\n")

print("==========================Magnitude=========================")
print("Vector")
a1 = Vector(1, 0, 0)
print(str(a1) + " :: " + str(a1.magnitude()))
a2 = Vector(0, 1, 0)
print(str(a2) + " :: " + str(a2.magnitude()))
a3 = Vector(0, 0, 1)
print(str(a3) + " :: " + str(a3.magnitude()))
a4 = Vector(1, 2, 3)
print(str(a4) + " :: " + str(a4.magnitude()))
a5 = Vector(-1, -2, -3)
print(str(a5) + " :: " + str(a5.magnitude()))
print("=====================================================\n\n")


print("==========================Normalize=========================")
print("Vector")
a1 = Vector(4, 0, 0)
print(str(a1) + " :: " + str(a1.normalize()))
a2 = Vector(1, 2, 3)
na2 = a2.normalize()
print(str(a2) + " :: " + str(na2))
print("normalized vector has magnitude: " + str(na2.magnitude()))
print("=====================================================\n\n")

print("==========================Dot Product=========================")
print("Vector . Vector")
a1 = Vector(1, 2, 3)
a2 = Vector(2, 3, 4)
print(str(a1) + " . " + str(a2) + " = " + str(a1.dot(a2)))
print("=====================================================\n\n")

print("==========================Cross Product=========================")
print("Vector x Vector")
a1 = Vector(1, 2, 3)
a2 = Vector(2, 3, 4)
print(str(a1) + " . " + str(a2) + " = " + str(a1.cross(a2)))
print(str(a2) + " . " + str(a1) + " = " + str(a2.cross(a1)))
print("=====================================================\n\n")
"""



