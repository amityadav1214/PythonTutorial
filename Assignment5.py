# Task 1 :- Write a Dictionary with Students marks. Key would be Student's Name and Marks as Value.
# We need to take student's name as input and retrive marks as output.
def student_marks():
    marks = {
        "Amit": 95,
        "Akshay": 78,
        "Aniket": 92
    }
    return marks

#Example usage
input_name = input("Enter student's name to get marks: ")
if input_name in student_marks():
    print("Marks for", input_name, "is", student_marks()[input_name])
else:
    print("Student not found.")

# Task 2 :- List Slicing    
def list_slicing(lst):
    return lst[0:5]

# Example usage
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sliced_list = list_slicing(lst)
print("Original list:", lst)
print("Sliced list (first 5 elements):", sliced_list)
print("Reverse Sliced list:", sliced_list[::-1])