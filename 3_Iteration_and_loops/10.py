# 10. Write an infinite while True loop simulating a server listening for requests. Use input("Enter command: "). If the command is "SHUTDOWN", break the loop and print "Server stopping...".



while True:
    command = input('Enter command: ')

    if command == 'SHUTDOWN':
        print('Server stopping.....')
        break