import numpy as np
import matplotlib.pyplot as plt
subjects = ['Math', 'Physics', 'Chemistry', 'English', 'Computer']
sem1 = np.array([85, 78, 92, 74, 88])
sem2 = np.array([90, 82, 89, 80, 91])
x = np.arange(len(subjects))
plt.figure(figsize=(10, 6))
plt.plot(x, sem1, marker='o', linestyle='-', color='blue', label='Semester 1')
plt.plot(x, sem2, marker='s', linestyle='--', color='green', label='Semester 2')
plt.xticks(x, subjects)
plt.title('Comparison of Semester 1 and 2 Results')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.ylim(60, 100)
plt.tight_layout()
plt.show()