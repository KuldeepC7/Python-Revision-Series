# 20. Password validation script: Take a string password = "pass123". Use a for loop to check each character. If a character is a space " ", break immediately and print "Invalid format". Use else to print "Valid format" if no spaces are found.

password = 'pass123'

for character in password:
    if character == ' ':
        print('Invalid format!')
        break
else:
    print('Valid format')