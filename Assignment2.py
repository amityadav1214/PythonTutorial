# Task 1 :- Check if the number is even or odd

number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")


# Task 2 :- Sum of Integers from 1 to 50 Using a Loop

integer_sum = 0
for i in range(1,51):
    integer_sum += i
print("The sum of the integers from range 1 to 50 is:", integer_sum)