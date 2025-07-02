import numpy as np
A = np.array([
    [1, -2,  3],
    [-1, 3, -1],
    [2, -5, 5]
])
B = np.array([9, -6, 17])
A_inv = np.linalg.inv(A)
solution_via_inverse = A_inv @ B
solution_via_solve = np.linalg.solve(A, B)
print("Solution using inverse matrix method:")
print(solution_via_inverse)
print("\nSolution using linalg.solve():")
print(solution_via_solve)