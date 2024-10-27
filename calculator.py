def addition(a, b):
    return a+b

def subtraction(a, b):
    return a-b

# Test the functions
num1 = float(input("Enter your number: "))
num2 = float(input("Enter your number: "))

# Multiplication
result_addition = addition(num1, num2)
print(f"Multiplication of {num1} and {num2} is: {result_addition}")

# Division
result_subtraction = subtraction(num1, num2)
print(f"Division of {num1} by {num2} is: {result_subtraction}")
