# 19. A simple command dispatcher: Write a while True loop that takes input(). If the input is empty, use pass (do nothing and prompt again). If it is "exit", break. Otherwise, print "Processing command".

while True:
    command = input('Enter your command: ')

    if command == '':
        pass

    elif command == 'exit':
        break

    else:
        print('Processing command')