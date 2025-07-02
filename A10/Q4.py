import numpy as np
arr = np.array([[6, -8, 73], [-1, 0, -5]])
arr[arr < 0] = 0
print(arr)