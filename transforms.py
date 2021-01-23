from matrix import Matrix
from vector import Vector
import numpy as np
from math import cos, sin, pi

def translation(x, y, z):
    return Matrix(np.array([[1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1]]))

def scaling(x, y, z):
    return Matrix(np.array([[x, 0, 0, 0], [0, y, 0, 0], [0, 0, z, 0], [0, 0, 0, 1]]))

def rotateX(rad):
    return Matrix(np.array([[1, 0, 0, 0], [0, cos(rad), -sin(rad), 0], [0, sin(rad), cos(rad), 0], [0, 0, 0, 1]]))
    
def rotateY(rad):
    return Matrix(np.array([[cos(rad), 0, sin(rad), 0], [0, 1, 0, 0], [-sin(rad), 0, cos(rad), 0], [0, 0, 0, 1]]))

def rotateZ(rad):
    return Matrix(np.array([[cos(rad), -sin(rad), 0, 0], [sin(rad), cos(rad), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))

def shearing(xy, xz, yx, yz, zx, zy):
    return Matrix(np.array([[1, xy, xz, 0], [yx, 1, yz, 0], [zx, zy, 1, 0], [0, 0, 0, 1]]))
    
