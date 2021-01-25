from intersections import Intersection
from vector import Vector

class Ray(object):
    def __init__(self, origin=Vector(0,0,0,1), direction=Vector(0,0,0)):
        self.origin = origin
        self.direction = direction
        self.intersections = []
        
    def getPosition(self, t):
        '''Given some t values, return the position on the ray line'''
        return self.origin + self.direction * t

    def addIntersection(self, t, obj):
        '''Add an Intersection object.  Sort t values from smallest to largest'''
        tvalues = [i.t for i in self.intersections]
        index = 0

        for el in tvalues:
            if el >= t:
                break
            index += 1
        self.intersections.insert(index, Intersection(t, obj))
    
    def hit(self):
        '''Given the list of Intersection objects, return the Intersection with smallest positive t'''
        for I in self.intersections:
            if I.t >= 0:
                return I
        return None

    def transform(self, M):
        '''Transform this ray by a transformation matrix M.'''
        origin = M * self.origin
        direction = M * self.direction
        return Ray(origin, direction)
