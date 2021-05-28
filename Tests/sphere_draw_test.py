import pygame
import sys
sys.path.insert(1, '..')
from canvas import Canvas
from color import Color
from vector import Vector
from ray import Ray
from sphere import Sphere
from transforms import *
from math import pi

WIDTH = 100
c = Canvas(WIDTH, WIDTH)
c.initializeScreen()

ray_origin = Vector(0, 0, -5, 1)
wall_z = 10.0
wall_size = 7.0
pixel_size = wall_size / WIDTH
half = wall_size / 2.0

s = Sphere()
S = scaling(0.5, 1, 1)
R = rotateZ(pi/4)
T = R * S
s.setTransform(T)

for y in range(WIDTH):
    print("Working")
    world_y = half - pixel_size * y
    for x in range(WIDTH):
        world_x = -half + pixel_size * x
        position = Vector(world_x, world_y, wall_z, 1)
        direction = position - ray_origin
        r = Ray(ray_origin, direction.normalize())
        xs = s.intersect(r)
        for t in xs:
            r.addIntersection(t, s)
        I = r.hit()
        if I is not None:
            print("Draw pixel")
            c.drawPixel(x, y, Color(1, 0, 0))
print("Finished")

while(True):
    c.update()
    





