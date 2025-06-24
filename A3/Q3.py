def is_palindrome(number):
    original_number = number
    reversed_number = 0
    while number > 0:
        remainder = number % 10
        reversed_number = (reversed_number * 10) + remainder
        number = number // 10
    return original_number == reversed_number
num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")