import pygame
from pygame.locals import *
from color import Color
import numpy as np

class Canvas(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.values = np.zeros(self.width*self.height, dtype=object).reshape((self.width, self.height))
        
    def initializeScreen(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height), 0, 32)
        for row in range(int(self.values.shape[0])):
            for col in range(int(self.values.shape[1])):
                self.values[row, col] = Color(0, 0, 0)
                
    def drawPixel(self, x, y, color):
        if 0 <= x < self.width:
            if 0 <= y < self.height:
                self.values[int(x), int(y)] = color
                pygame.draw.circle(self.screen, color.color255(), (int(x), int(y)), 0)

    def readPixel(self, x, y):
        return self.values[x, y]

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        pygame.display.update()
