# 6. You are building an admin panel login. Write an infinite while True loop that repeatedly asks for a password using input(). If the password is "admin123", use break to exit the loop and print "Access Granted".

pas = 'admin123'

while True:
    password = input("Enter admin password: ")
    
    if password == pas:
        print('Correct password :)')
        break
    else:
        print('Wrong password, try again!')
        