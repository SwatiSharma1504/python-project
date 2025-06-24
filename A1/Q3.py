def calculate_student_percentage():
    name = input("Enter student name: ")
    stu_class = input("Enter class: ")
    marks = []
    for i in range(5):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i+1}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Invalid input. Marks should be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    total_marks = sum(marks)
    percentage = (total_marks / 500) * 100
    print("\n--- Student Result ---")
    print(f"Name: {name}")
    print(f"Class: {stu_class}")
    print(f"Total Marks: {total_marks}")
    print(f"Percentage: {percentage:.2f}%")
if __name__ == "__main__":
    calculate_student_percentage()