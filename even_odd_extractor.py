# Write a Python program that reads a text file named numbers.txt that contains 20 integers. 
# The program will create two other text file; the first text file will be named even.txt that will 
# ontains all even numbers extracted from the numbers.txt. The second text file will be named odd.txt 
# that will contains all odd numbers extracted from the numbers.txt.

import pyfiglet
import time
# Defining variables
intro = pyfiglet.figlet_format("WELCOME".center(39, "="), font = "digital")
# Open the input file and read the numbers
with open("numbers.txt", "r") as input_file:
    numbers = input_file.readlines()
# Convert the numbers to integers
numbers = [int(num) for num in numbers]
# Extract even and odd numbers
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

with open("even.txt", "w") as even_file, open("odd.txt", "w") as odd_file:
    even_file.write("These are the even numbers in the file:" + "\n")
    # Write even numbers to even.txt
    for num in even_numbers:
        even_file.write(str(num) + "\n")
    # Write odd number to odd.txt
    odd_file.write("These are the odd numbers in the file:" + "\n")
    for num in odd_numbers:
        odd_file.write(str(num) + "\n")
# Display the confirmation message
