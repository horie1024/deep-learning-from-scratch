import numpy as np

# 2 × 2
A = np.array([[1,2], [3,4]])
print(A.shape)

B = np.array([[5,6], [7,8]])
print(B.shape)

print(np.dot(A,B))

# 3 × 2
C = np.array([[1,2,3], [4,5,6]])
print(C.shape)

D = np.array([[1,2], [3,4], [5,6]])
print(D.shape)

print(np.dot(C, D))
