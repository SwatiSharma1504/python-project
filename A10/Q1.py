import numpy as np
arr = np.array([
    [6, -8, 73, -110],
    [np.nan, -8, 0, 94],
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
arr = np.nan_to_num(arr)
submatrix = arr[:3, :3]
transposed = submatrix.T
print("Original array with NaN replaced:")
print(arr)
print("\n3x3 submatrix:")
print(submatrix)
print("\nTransposed 3x3 submatrix:")
print(transposed)