import sys
sys.path.insert(1, '..')
from ray import Ray
from vector import Vector

print("=====================================================")
p = Vector(1, 2, 3, 1)
d = Vector(4,5,6)
r = Ray(p, d)
print(r.origin)
print(r.direction)



