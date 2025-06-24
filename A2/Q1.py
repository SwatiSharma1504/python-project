student_name = input("Enter the student's name: ")
student_class = input("Enter the student's class: ")
print("Enter marks for 5 subjects:")
marks = []
for i in range(1, 6):
    mark = float(input(f"  Subject {i} marks: "))
    marks.append(mark)
total_marks = sum(marks)
percentage = (total_marks / 500) * 100
print("\n--- Student Result ---")
print(f"Name      : {student_name}")
print(f"Class     : {student_class}")
print(f"Percentage: {percentage:.2f}%")