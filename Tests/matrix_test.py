import sys
sys.path.insert(1, '..')
#sys.path.insert(1, 'C:\\Users\\admin\\Documents\\RayTracing_Challenge')
from matrix import Matrix
from vector import Vector
import numpy as np

print("=====================================================")
vals = np.array([[1,2,3,4],[5.5,6.5,7.5,8.5],[9,10,11,12],[13.5,14.5,15.5,16.5]])
M = Matrix(vals)
print(vals)
print(M)
print("")

vals = np.array([[1,2,3],[5.5,6.5,7.5],[9,10,11]])
M = Matrix(vals)
print(vals)
print(M)
print("")

vals = np.array([[1,2],[5.5,6.5]])
M = Matrix(vals)
print(vals)
print(M)

print("\n===============MATRIX EQUALITY=======================")
m1 = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,6],[5,4,3,2]])
m2 = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,6],[5,4,3,2]])
m3 = np.array([[2,3,4,5],[5,6,7,8],[9,8,7,6],[5,4,3,2]])
m4 = np.array([[1,2,3,4.002],[5.000001,6,7,8],[9,8,7,6],[5,4,3,2]])

M1 = Matrix(m1)
M2 = Matrix(m2)
M3 = Matrix(m3)
M4 = Matrix(m4)

print("M1 == M2: " + str(M1 == M2))
print("M2 == M1: " + str(M2 == M1))
print("M1 == M3: " + str(M1 == M3))
print("M2 == M3: " + str(M2 == M3))
print("M1 == M4: " + str(M1 == M4))

print("\n===============MATRIX MULTIPLY=======================")
m1 = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,6],[5,4,3,2]])
m2 = np.array([[-2,1,2,3],[3,2,1,-1],[4,3,6,5],[1,2,7,8]])
M1 = Matrix(m1)
M2 = Matrix(m2)
print("M1 x M2 = " + str(M1 * M2))

print("\nMatrix times vector\n")
m = np.array([[1,2,3,4],[2,4,4,2],[8,6,4,1],[0,0,0,1]])
M = Matrix(m)
v = Vector(1,2,3,1)
print("M x v = " + str(M * v))

print("\n===============IDENTITY MATRIX MULTIPLY=======================")
m1 = np.array([[0,1,2,4],[1,2,4,8],[2,4,8,16],[4,8,16,32]])
m2 = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
M1 = Matrix(m1)
I = Matrix(m2)
V = M1 * I
print("M1 x I = " + str(V))
print("M1 = I = " + str(M1 == V))

a = Vector(1, 2, 3, 4)
b = I * a
print("I * a = " + str(b))
print("a = b: " + str(a == b))


print("\n===============MATRIX TRANSFORMATION=======================")
m1 = np.array([[0,1,2,4],[1,2,4,8],[2,4,8,16],[4,8,16,32]])
m2 = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
M1 = Matrix(m1)
I = Matrix(m2)

print(M1)
print(M1.transpose())

print("\n")
print(I)
print(I.transpose())

print("\n=================DETERMINANT==============================")
m = np.array([[1,5],[-3,2]])
M = Matrix(m)
print(M)
print("Determinant = " + str(M.determinant()))


print("\n===================SUBMATRICES============================")
m = np.array([[1, 5, 0], [-3, 2, 7], [0, 6, -3]])
M = Matrix(m)
print(M)
print("Remove row 0 and column 2")
print(M.submatrix(0, 2))

m = np.array([[-6, 1, 1, 6], [-8, 5, 8, 6], [-1, 0, 8, 2], [-7, 1, -1, 1]])
M = Matrix(m)
print(M)
print("Remove row 2 and column 1")
print(M.submatrix(2, 1))


print("\n===================MINOR OF 3X3 MATRIX==================\n")
m = np.array([[3, 5, 0], [2, -1, -7], [6, -1, 5]])
M = Matrix(m)
print(M)
print("Minor at row 1 column 0 is: " + str(M.minor(1, 0)))

print("\n===================COFACTOR OF 3X3 MATRIX==================\n")
m = np.array([[3, 5, 0], [2, -1, -7], [6, -1, 5]])
M = Matrix(m)
print(M)
print("Minor at row 0 column 0 is: " + str(M.minor(0, 0)))
print("Cofactor at row 0 column 0 is: " + str(M.cofactor(0, 0)))
print("Minor at row 1 column 0 is: " + str(M.minor(1, 0)))
print("Cofactor at row 1 column 0 is: " + str(M.cofactor(1, 0)))

print("\n===================DETERMINANT OF 3X3 MATRIX==================\n")
m = np.array([[1, 2, 6], [-5, 8, -4], [2, 6, 4]])
M = Matrix(m)
print(M)
print("Cofactor at row 0 column 0 is: " + str(M.cofactor(0, 0)))
print("Cofactor at row 0 column 1 is: " + str(M.cofactor(0, 1)))
print("Cofactor at row 0 column 2 is: " + str(M.cofactor(0, 2)))
print("Determinant = " + str(M.determinant()))

print("\n===================DETERMINANT OF 4X4 MATRIX==================\n")
m = np.array([[-2, -8, 3, 5], [-3, 1, 7, 3], [1, 2, -9, 6], [-6, 7, 7, -9]])
M = Matrix(m)
print(M)
print("Cofactor at row 0 column 0 is: " + str(M.cofactor(0, 0)))
print("Cofactor at row 0 column 1 is: " + str(M.cofactor(0, 1)))
print("Cofactor at row 0 column 2 is: " + str(M.cofactor(0, 2)))
print("Cofactor at row 0 column 3 is: " + str(M.cofactor(0, 3)))
print("Determinant = " + str(M.determinant()))

print("\n===================DETERMINANT OF 4X4 MATRIX==================\n")
m = np.array([[6,4,4,4], [5,5,7,6], [4,-9,3,-7], [9,1,7,-6]])
M = Matrix(m)
print(M)
print("Determinant: " + str(M.determinant()))

m = np.array([[-4,2,-2,-3], [9,6,2,6], [0,-5,1,-5], [0,0,0,0]])
M = Matrix(m)
print(M)
print("Determinant: " + str(M.determinant()))


print("\n=================INVERSE===============================\n")
m = np.array([[-5, 2, 6, -8], [1, -5, 1, 8], [7, 7, -6, -7], [1, -3, 7, 4]])
M = Matrix(m)
print(M)
print("\nInverse")
B = M.inverse()
print(B)
print("Determinant = " + str(M.determinant()))
print("Cofactor at 2 3 = " + str(M.cofactor(2, 3)))
print("Cofactor at 3, 2 = " + str(M.cofactor(3, 2)))

m = np.array([[8, -5, 9, 2], [7, 5, 6, 1], [-6, 0, 9, 6], [-3, 0, -9, -4]])
M = Matrix(m)
print(M)
print("\nInverse")
B = M.inverse()
print(B)

m = np.array([[9, 3, 0, 9], [-5, -2, -6, -3], [-4, 9, 6, 4], [-7, 6, 6, 2]])
M = Matrix(m)
print(M)
print("\nInverse")
B = M.inverse()
print(B)

a = np.array([[3, -9, 7, 3], [3, -8, 2, -9], [-4, 4, 4, 1], [-6, 5, -1, 1]])
b = np.array([[8, 2, 2, 2], [3, -1, 7, 0], [7, 0, 5, 4], [6, -2, 0, 5]])
A = Matrix(a)
B = Matrix(b)
print(A)
print(B)
print("\nInverse")
C = A * B
print("A x B")
print(C)
BI = B.inverse()
print(BI)
Atest = C * BI
print(Atest)
print(A == Atest)
print(B * BI)
print(BI * B)


