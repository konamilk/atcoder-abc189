import numpy as np
N = int(input())
A = np.array(list(map(int, input().split())))

Amin = A.min()
result = A.min() * len(A)
