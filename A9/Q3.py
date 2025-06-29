import numpy as np
arr = np.array([1, 2, 3, 4, 5])
reversed_arr = arr[::-1]
print(reversed_arr)
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
reversed_rows = arr2d[::-1]
print(reversed_rows)
reversed_cols = arr2d[:, ::-1]
print(reversed_cols)
reversed_both = arr2d[::-1, ::-1]
print(reversed_both)