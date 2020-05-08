import numpy as np
import math

def construct_matrix(x, y):
    A = np.zeros((len(y), len(x))) # construct a zero matrix of m,n
    for i in range(1, len(y+1)):
        for j in range(1, len(x+1)):
            A[i][j] = math.cos(y[i] + x[j]) # fill in the matrix entry with the cosine function
    return A

def answer(m, n):
    rank = list()
    for i in range(100): # generate 100 matrices
        y = np.random.rand(m) * math.pi # a list of uniform random numbers between 0 and 2pi
        x = np.random.rand(n) * math.pi # a list of uniform random numbers between 0 and 2pi
        matrix = construct_matrix(x, y) # calling the above construct matrix method
        rank.append(np.linalg.matrix_rank(matrix))
    return rank

m = 3
n =5
ranks = answer(m, n)
print('Avg. rank :', np.mean(ranks))
print(ranks)
