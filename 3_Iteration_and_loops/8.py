# 8. Python has a unique for...else construct perfect for searching. Write a for loop that iterates through the string "DATABASE". If it finds the letter "X", it should break. If the loop finishes without finding "X" (meaning it never broke), the else block should print "Clean data".

db = 'DATABASE'

for character in db:
    if character == 'X':
        break

    print(character)

else:
    print('Clean data')