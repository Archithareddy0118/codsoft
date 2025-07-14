# Basic Arithmetic Operations in Python

# Input two numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Perform operations
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b if b != 0 else "Cannot divide by zero")
print("Modulus:", a % b if b != 0 else "Cannot perform modulus with zero")