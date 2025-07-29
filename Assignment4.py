# Task 1 : Opens and reads a text file and writing in a TRY EXCEPT block

try:
    file = open('sample.txt', 'r')
    content = file.read()
    file.close()
    print(content)
except FileNotFoundError:
    print("File not found")

# Task 2 :  Write and Append Data to a File

try:
    file = open('sample.txt', 'w')
    content = input("Enter content to write to the file: ")
    file.write(content)
    file.close()
    print("Content written successfully in sample.txt")
    file = open('sample.txt', 'a')
    content = input("Enter additional content to write to the file: ")
    file.write(content)
    file.close()
    print("Data successfully appended to sample.txt")
    print("Final content of the file:")
    file = open('sample.txt', 'r')
    content = file.read()
    file.close()
    print(content)
except FileNotFoundError:
    print("File not found")