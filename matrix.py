from copy import deepcopy
import numpy as np
from vector import Vector
"""
data should be a numpy array.  
"""
class Matrix(object):
    def __init__(self, data=None, n=0, m=0):
        if data is None:
            data = np.zeros(n*m).reshape((n, m))
        self.data = data
        self.n, self.m = self.data.shape
        self.epsilon = 0.00001

    def __str__(self):
        return "Matrix["+str(self.n)+"x"+str(self.m)+"]\n" + str(self.data)
    
    def __eq__(self, other):
        if self.n == other.n  and self.m == other.m:
            for row in range(self.n):
                for col in range(self.m):
                    val = self.data[row, col] - other.data[row, col]
                    if abs(val) > self.epsilon:
                        return False
            return True
        return False

    def __mul__(self, other):
        '''Matrix multiplication:  nxm X mxq = nxq'''
        if type(other) == Vector:
            c = np.array(other.asTuple()).reshape((len(other.asTuple()), 1))
            B = Matrix(c)
        else:
            B = other
            
        if self.m == B.n:
            C = Matrix(n=self.n, m=B.m)
            for i in range(self.n):
                for j in range(B.m):
                    s = 0
                    for k in range(self.m):
                        s += self.data[i,k] * B.data[k,j]
                    C.data[i, j] = s

        if type(other) == Vector:
            c = C.data.flatten()
            C = Vector(*c)
        return C

    def transpose(self):
        '''Transpose this Matrix.  Does not modify this matrix'''
        M = Matrix(n=self.n, m=self.m)
        for i in range(self.n):
            for j in range(self.m):
                M.data[i, j] = self.data[j, i]
        return  M
        #T = self.data.T
        #return Matrix(T)

    def determinant(self):
        '''Find the determinant of a 2x2 Matrix'''
        det = 0
        if self.m == 2 and self.n == 2:
            det = self.data[0,0] * self.data[1,1] - self.data[0,1]*self.data[1, 0]
        else:
            for j in range(self.m):
                det += self.cofactor(0, j) * self.data[0, j]
        return det

    def submatrix(self, row, column):
        '''Return a Matrix where the row and column of this matrix is removed'''
        L = []
        for i in range(self.n):
            for j in range(self.m):
                if i != row and j != column:
                    L.append(self.data[i, j])
        #print(L)
        M = Matrix(np.array(L).reshape((self.n-1, self.m-1)))
        return M

    def minor(self, row, column):
        '''Minor of a 3x3 matrix is the determinant of its submatrix given by the row and column'''
        #if self.n == 3 and self.m == 3:
        M = self.submatrix(row, column)
        return M.determinant()

    def cofactor(self, row, column):
        minor = self.minor(row, column)
        if (row + column) % 2 == 1:
            minor *= -1
        return minor

    def inverse(self):
        '''Return the inverse of this Matrix.  Or None if this Matrix is not invertible'''
        M = Matrix(n=self.n, m=self.m)
        det = self.determinant()
        if det != 0:
            for i in range(self.n):
                for j in range(self.m):
                    M.data[j, i] = self.cofactor(i, j) / det
        return M
