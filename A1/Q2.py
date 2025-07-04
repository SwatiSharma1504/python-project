def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose an operation (+, -, *, /): ")
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                result = "Error: Cannot divide by zero."
            else:
                result = num1 / num2
        else:
            result = "Invalid operation."
        print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter numbers only.")
calculator()