"""
Advanced Calculator Module

This module provides basic arithmetic operations along with additional features:
- Addition
- Subtraction
- Multiplication
- Division
- Exponentiation
- Square Root
- Percentage Calculation

Created by: Mohammed Kolo Ibraim
"""

import math

def add(a, b):
    """
    Adds two numbers and prints the result.
    """
    answer = a + b
    print(f"{a} + {b} = {answer}")

def sub(a, b):
    """
    Subtracts two numbers and prints the result.
    """
    answer = a - b
    print(f"{a} - {b} = {answer}")

def mul(a, b):
    """
    Multiplies two numbers and prints the result.
    """
    answer = a * b
    print(f"{a} * {b} = {answer}")

def div(a, b):
    """
    Divides two numbers and prints the result.
    """
    if b == 0:
        print("Error: Division by zero!")
    else:
        answer = a / b
        print(f"{a} / {b} = {answer}")

def exp(a, b):
    """
    Calculates a raised to the power of b and prints the result.
    """
    answer = a ** b
    print(f"{a} ^ {b} = {answer}")

def sqrt(a):
    """ 
    Calculates the square root of a number and prints the result.
    """
    if a < 0:
        print("Error: Cannot calculate square root of a negative number.")
    else:
        answer = math.sqrt(a)
        print(f"√{a} = {answer:.4f}")

def percentage(a, percent):
    """
    Calculates the percentage of a number and prints the result.
    """
    result = (percent / 100) * a
    print(f"{percent}% of {a} = {result:.4f}")

print("A, Addition")
print("B, Subtraction")
print("C, Multiplication")
print("D, Division")
print("E, Exponentiation")
print("F, Square Root")
print("G, Percentage Calculation")
print("H, Exit")

while True:
    choice = input("Input your choice: ").strip().lower()

    if choice == 'a':
        a = float(input("Input first number: "))
        b = float(input("Input second number: "))
        add(a, b)
    elif choice == 'b':
        a = float(input("Input first number: "))
        b = float(input("Input second number: "))
        sub(a, b)
    elif choice == 'c':
        a = float(input("Input first number: "))
        b = float(input("Input second number: "))
        mul(a, b)
    elif choice == 'd':
        a = float(input("Input first number: "))
        b = float(input("Input second number: "))
        div(a, b)
    elif choice == 'e':
        a = float(input("Input base number: "))
        b = float(input("Input exponent: "))
        exp(a, b)
    elif choice == 'f':
        a = float(input("Input a non-negative number: "))
        sqrt(a)
    elif choice == 'g':
        a = float(input("Input the total value: "))
        percent = float(input("Input the percentage (0-100): "))
        percentage(a, percent)
    elif choice == 'h':
        print("Program ended")
        break
    else:
        print("Invalid choice. Please choose again.")
