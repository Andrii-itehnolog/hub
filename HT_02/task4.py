"""  Write a script which accepts a <number> from user and then <number> times asks user for string input. 
At the end script must print out result of concatenating all <number> strings.
"""

number = int(input("Please enter number: "))
line = ""
for i in range(number):
    new_line = input("Please, enter your string: ")
    line += new_line
print(f"Concatenated string is:\n {line}")


