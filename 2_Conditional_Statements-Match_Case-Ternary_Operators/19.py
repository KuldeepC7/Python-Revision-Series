# 19. Password validation backend: Write an if/else structure that first checks if len(password) > 8. If it is, use an inner if/else to check if the string "!" or "@" is present in the password, setting is_strong = True if so.

password = input('Enter password: ')
is_strong = False

if len(password) > 8:
    if '!' in password or '@' in password:
        is_strong = True

print(is_strong)