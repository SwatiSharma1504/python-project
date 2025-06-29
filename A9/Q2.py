import numpy as np
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])
arr1d = arr2d.flatten()
print(arr1d)
arr1d = arr2d.ravel()
print(arr1d)
arr1d = arr2d.reshape(-1)
print(arr1d)