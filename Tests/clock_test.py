import pygame
import sys
sys.path.insert(1, '..')
from canvas import Canvas
from color import Color
from transforms import *
from matrix import Matrix
from vector import Vector
from math import pi

c = Canvas(500, 500)
c.initializeScreen()

#c.drawPixel(2, 3, Color(1, 0, 0))

p = Vector(0, -1, 0, 1)
T = translation(250, 250, 0)
S = scaling(200, 200, 0)

for i in range(12):
    R = rotateZ(i * pi / 6)
    pnew = T * S * R * p
    c.drawPixel(pnew.x, pnew.y, Color(1, 1, 1))

while(True):
    c.update()
    





