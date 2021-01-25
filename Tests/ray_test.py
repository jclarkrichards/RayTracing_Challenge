import sys
sys.path.insert(1, '..')
from ray import Ray
from sphere import Sphere
from vector import Vector
from intersections import Intersection
from transforms import *

print("=====================================================")
p = Vector(1, 2, 3, 1)
d = Vector(4,5,6)
r = Ray(p, d)
print(r.origin)
print(r.direction)

print("\n==========Computing a point from a distance============\n")
r = Ray(Vector(2,3,4,1), Vector(1, 0, 0))
print(r.getPosition(0))
print(r.getPosition(1))
print(r.getPosition(-1))
print(r.getPosition(2.5))


print("\n========A Ray intersects a Sphere at 2 points=========")
r = Ray(Vector(0, 0, -5, 1), Vector(0, 0, 1))
s = Sphere()
xs = s.intersect(r)
print("Number of intersections = " + str(len(xs)))
print(xs);

print("\n========A Ray intersects a Sphere at 1 point at tangent========")
r = Ray(Vector(0, 1, -5, 1), Vector(0, 0, 1))
s = Sphere()
xs = s.intersect(r)
print("Number of intersections = " + str(len(xs)))
print(xs);

print("\n========A Ray misses a Sphere entirely========")
r = Ray(Vector(0, 2, -5, 1), Vector(0, 0, 1))
s = Sphere()
xs = s.intersect(r)
print("Number of intersections = " + str(len(xs)))
print(xs);

print("\n========A Ray starts inside a sphere========")
r = Ray(Vector(0, 0, 0, 1), Vector(0, 0, 1))
s = Sphere()
xs = s.intersect(r)
print("Number of intersections = " + str(len(xs)))
print(xs);

print("\n========A Sphere is behind the Ray========")
r = Ray(Vector(0, 0, 5, 1), Vector(0, 0, 1))
s = Sphere()
xs = s.intersect(r)
print("Number of intersections = " + str(len(xs)))
print(xs);


print("\n==========Aggregating Intersections===========")
r = Ray(Vector(0,0,-5,1), Vector(0,0,1))
s = Sphere()
ts = s.intersect(r)
for t in ts:
    r.addIntersection(t, s)
print(r.intersections[0].obj)
print(r.intersections[1].obj)
#r.addIntersection(1, s)
#r.addIntersection(2, s)
#print(len(r.intersections))
#print(r.intersections[0].t)
#print(r.intersections[1].t)

print("\n===============IDENTIFYING HITS=============\n")
print("When all intersections have positive t values")
s = Sphere()
r = Ray()
r.addIntersection(1, s)
r.addIntersection(2, s)
I = r.hit()
print(I.t)

print("When all intersections have positive t values")
s = Sphere()
r = Ray()
r.addIntersection(-1, s)
r.addIntersection(1, s)
I = r.hit()
print(I.t)

print("When all intersections have positive t values")
s = Sphere()
r = Ray()
r.addIntersection(-2, s)
r.addIntersection(-1, s)
I = r.hit()
if I is not None:
    print(I.t)
else:
    print("NONE")

print("When all intersections have positive t values")
s = Sphere()
r = Ray()
r.addIntersection(5, s)
r.addIntersection(7, s)
r.addIntersection(-3, s)
r.addIntersection(2, s)
I = r.hit()
print(I.t)



print("Translating a ray")
r = Ray(Vector(1,2,3,1), Vector(0,1,0))
M = translation(3,4,5)
r2 = r.transform(M)
print(r.origin)
print(r.direction)
print("r2")
print(r2.origin)
print(r2.direction)

print("\nScaling a ray")
r = Ray(Vector(1,2,3,1), Vector(0,1,0))
M = scaling(2,3,4)
r2 = r.transform(M)
print(r.origin)
print(r.direction)
print("r2")
print(r2.origin)
print(r2.direction)

print("\nSphere default transformation")
s = Sphere()
print(s.transform)
M = translation(2, 3, 4)
s.setTransform(M)
print(s.transform)


print("\n\nIntersecting a scaled sphere with a ray")
r = Ray(Vector(0, 0, -5, 1), Vector(0, 0, 1))
s = Sphere()
s.setTransform(scaling(2, 2, 2))
xs = s.intersect(r)
print(xs)
print(len(xs))
print("-----------")
for x in xs:
    r.addIntersection(x, s)
print(r.intersections[0].t)
print(r.intersections[1].t)


print("\n\nIntersecting a translated sphere with a ray")
r = Ray(Vector(0, 0, -5, 1), Vector(0, 0, 1))
s = Sphere()
s.setTransform(translation(5, 0, 0))
xs = s.intersect(r)
print(len(xs))






