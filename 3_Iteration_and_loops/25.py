# 25. Cryptographic Prime Checker: A backend security module needs to verify if a number is prime to generate keys. Ask for an integer via input(). Use a for loop from 2 up to number // 2. If the number is evenly divisible by the loop variable, break (it's not prime). Use the else clause to confidently declare it a prime number.

number = int(input('Enter a number: '))

for i in range(2, number // 2):
    if (number % i == 0):
        print('Not a prime number!')
        break

else:
    print('Prime number :)')