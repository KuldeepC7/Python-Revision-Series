# 16. Write a while loop to calculate the mathematical factorial of a number provided via input(). (e.g., if the user enters 5, calculate 5 * 4 * 3 * 2 * 1).

number = int(input('Enter the number of which you want factorial: '))
factorial = 1

while number != 0:
    factorial *= number
    number -= 1

print(factorial)