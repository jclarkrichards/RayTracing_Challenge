from vector import Vector
from math import sqrt
#from intersections import Intersection
from transforms import Identity4x4
from material import Material

class Sphere(object):
    def __init__(self, origin=Vector(0, 0, 0, 1), radius=1):
        self.origin = origin
        self.radius = radius
        self.transform = Identity4x4()
        self.material = Material()
        
    def intersect(self, ray):
        rayInv = ray.transform(self.transform.inverse())
        origins = rayInv.origin - self.origin
        a = rayInv.direction.dot(rayInv.direction)
        b = 2 * rayInv.direction.dot(origins)
        c = origins.dot(origins) - 1
        discriminant = b*b - 4 * a * c
        ts = []
        if discriminant >= 0:
            disq = sqrt(discriminant)
            ts.append((-b - disq) / (2 * a))
            ts.append((-b + disq) / (2 * a))
            ts.sort()
        return ts

    def setTransform(self, T):
        self.transform = T
        
    def getNormal(self, point):
        '''Given a point on the sphere, return the normal'''
        TI = self.transform.inverse()
        obj_point = TI * point
        obj_normal = obj_point - self.origin
        world_normal = TI.transpose() * obj_normal
        world_normal.w = 0
        return world_normal.normalize()
