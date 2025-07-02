import numpy as np
arr = np.random.randint(0, 10, (2, 3, 4))  # shape: (2, 3, 4)
print("Original shape:", arr.shape)
moved = np.moveaxis(arr, 0, 2)
print("New shape after moveaxis:", moved.shape)
transposed = np.transpose(arr, (2, 0, 1))
print("New shape after transpose:", transposed.shape)
