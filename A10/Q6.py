import numpy as np
arr1 = np.array([3, 4])
arr2 = np.array([1, 0])
avg = (arr1 + arr2) / 2
print("Average of numpy arrays:\n", avg)
from scipy import stats
a1 = np.array([[1, 2, 3], [4, 5, 6]])
a2 = np.array([[6, 5, 4], [3, 2, 1]])
avg_2d = (a1 + a2) / 2
mean_val = np.mean(avg_2d)
median_val = np.median(avg_2d)
mode_val = stats.mode(avg_2d, axis=None, keepdims=False).mode
print("2D Average:\n", avg_2d)
print("Mean:", mean_val)
print("Median:", median_val)
print("Mode:", mode_val)