# 28. Brute Force Defense: You know a secret admin PIN is exactly 3 digits. Write a for loop using range(1000) to guess the pin. Take the "actual pin" via input() before the loop starts. Stop the loop when the guess matches the actual pin, and print exactly how many attempts it took.

PIN = int(input('Enter your admin pin: '))

for guess in range(1000):
    if guess == PIN:
        print(guess)