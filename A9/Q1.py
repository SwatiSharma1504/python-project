import numpy as np
arr1d = np.array([10, 20, 30])
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])
result = np.vstack([arr2d, arr1d])
print(result)
arr1d_col = arr1d.reshape(-1, 1)[:2]
result = np.hstack([arr2d, arr1d_col])
print(result)
arr1d_reshaped = arr1d[np.newaxis, :]
result = np.concatenate((arr2d, arr1d_reshaped), axis=0)
print(result)