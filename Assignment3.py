# Task 1 :- To find Factorial of a number
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n * factorial(n-1)

# result = int(input("Enter a number to find its factorial: "))
# print(f"The factorial of {result} is: {factorial(result)}")

# Task 2 :- Usage of Math Module
import math
# Calculate the square root of a number
number = float(input("Enter a number: "))
square_root = math.sqrt(number)
print(f"The square root of {number} is: {square_root}")

# Calculate Natural logarithm (log base e) of the number
natural_log = math.log(number)
print(f"The natural logarithm (base e) of {number} is: {natural_log}")

# Calculate Sine of the number (in radians)
sine_value = math.sin(number)
print(f"The sine of {number} (in radians) is: {sine_value}")
