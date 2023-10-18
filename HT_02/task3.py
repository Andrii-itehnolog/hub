"""  Write a script which accepts a <number> from user and print out a sum of the first <number> positive integers."""

number = int(input("Please enter number: "))
summ = 0
for i in range(1, number+1):
    summ += i
print(f"Sum of the first {number} positive integers equals {summ}")


