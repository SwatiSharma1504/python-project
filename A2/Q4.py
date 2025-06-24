student_name = input("Enter the student's name: ")
student_class = input("Enter the student's class: ")
print("Enter marks for 5 subjects:")
marks = []
grades = []
for i in range(1, 6):
    mark = float(input(f"  Subject {i} marks: "))
    marks.append(mark)
    if mark >= 60:
        grade = 'A'
    elif mark >= 50:
        grade = 'B'
    elif mark >= 40:
        grade = 'C'
    elif mark >= 33:
        grade = 'D'
    else:
        grade = 'Fail'
    grades.append(grade)
total_marks = sum(marks)
percentage = (total_marks / 500) * 100
print("\n--- Student Result ---")
print(f"Name      : {student_name}")
print(f"Class     : {student_class}")
print(f"Total     : {total_marks} / 500")
print(f"Percentage: {percentage:.2f}%\n")
print("--- Subject-wise Grades ---")
for i in range(5):
    print(f"Subject {i+1}: Marks = {marks[i]}, Grade = {grades[i]}")