# 29. Load Balancer Routing: Use a while True loop. Take input("Incoming request to (API/WEB/DB) or STOP: "). Use continue if the input is "DB" (refusing direct database access). Use break if it is "STOP". Otherwise, print "Routing to [input]".


while True:
    request = input('Incoming request to (API/WEB/DB) or STOP: ')
    
    if request == 'DB':
        continue
    elif request == 'STOP':
        break
    else:
        print(f'Routng to {request}')