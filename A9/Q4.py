import numpy as np
arr = np.array([[3, 5, 7],
                [2, 8, 1],
                [6, 4, 9]])
max_value = np.max(arr)
print("Maximum value:", max_value)
min_value = np.min(arr)
print("Minimum value:", min_value)
rows, cols = arr.shape
print("Rows:", rows, "Columns:", cols)
for row in arr:
    for element in row:
        print(element, end=' ')
specific_element = arr[1][2]  # Indexing starts at 0
print("Specific element:", specific_element)
total_sum = 0
for row in arr:
    for val in row:
        total_sum += val
print("Sum using for loop:", total_sum)
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
add_result = arr + arr2
print("Addition:\n", add_result)
sub_result = arr - arr2
print("Subtraction:\n", sub_result)
mul_result = arr * arr2  # Element-wise multiplication
print("Multiplication:\n", mul_result)
div_result = arr / arr2
print("Division:\n", div_result)