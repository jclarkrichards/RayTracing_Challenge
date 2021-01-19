import pygame
import sys
sys.path.insert(1, 'C:\\Users\\admin\\Documents\\RayTracing_Challenge')
from canvas import Canvas
from vector import Vector, Point
from color import Color

#pygame.init()
WIDTH, HEIGHT = (900, 550)
c = Canvas(WIDTH, HEIGHT)
c.initializeScreen()

p = Point(0, 0, 0)
v = Vector(1, 1.8, 0)
v = v.normalize()
v *= 11.25
g = Vector(0, -.1, 0)
w = Vector(-.01, 0, 0)

while p.y >= 0:
    c.drawPixel(p.x, HEIGHT-p.y, Color(1,0,0))
    p += v
    v += g + w

while True:
    c.update()

