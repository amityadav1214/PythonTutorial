# Problem 1 :- Reverse a String without using Reverse function

# def reverse_string(s):
#     reversed_s = ""
#     for char in s:
#         reversed_s = char + reversed_s
#     return reversed_s

# # Example usage
# input_string = input("Enter a string to reverse: ")
# reversed_string = reverse_string(input_string)
# print("Reversed string:", reversed_string)

# Problem 2 :- Check String is palindrome or not
# def palindrome(s):
#     reversed_s = ""
#     for char in s:
#         reversed_s = char + reversed_s
#     return s == reversed_s


# # Example usage
# input_string = input("Enter a string to check if it is Palindrome: ")
# palindrome = palindrome(input_string)
# print("Reversed string:", palindrome)

# Problem 3 :- Check if a String contains count of vowels.
# def vowels(s):
#     count = 0
#     for char in s:
#         if char.lower() in 'aeiou':
#             count += 1
#     return count
        
# # Example usage
# input_string = input("Enter a string to count vowels: ")
# vowel_count = vowels(input_string)
# print("Number of vowels in the string:", vowel_count)

# Problem 4 :- Find a Maximum number in a list without using max()
# def find_max(lst):
#     if not list:
#         return None
#     max_num = lst[0]
#     for num in lst:
#         if num > max_num:
#             max_num = num
#     return max_num

# # Example usage
# input_list = list(map(int, input("Enter numbers separated by space: ").split()))
# max_number = find_max(input_list)
# print("Maximum number in the list:", max_number)

# Problem 5 :- Print numbers from 1 to 50. For multiples of 3, print "Fizz", 
# for multiples of 5, print "Buzz", and for multiples of both, print "FizzBuzz".

def fizz_buzz():
    for i in range(1,51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Example usage
fizz_buzz()
