"""Write a script which accepts a <number> from user and generates dictionary in range <number> 
where key is <number> and value is <number>*<number>
e.g. 3 --> {0: 0, 1: 1, 2: 4, 3: 9}.
"""

number = int(input("Please enter the number of dict items: "))
dict_of_numbers = dict()
for i in range(number+1):
    dict_of_numbers[i] = i * i
print(f"Generated dict is:\n{dict_of_numbers}")





