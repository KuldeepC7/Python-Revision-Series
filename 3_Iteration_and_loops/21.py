# 21. Exponential Backoff Algorithm: This is a crucial backend concept for database connections. Write a while loop that attempts to connect 5 times. Start with a delay = 1 second. Inside the loop, ask for input("Connection status (ok/fail): "). If "ok", break. If "fail", multiply the delay by 2 and continue. If all 5 attempts fail, use the else clause to print "Server unreachable".

import time

attempts = 1
delay = 1

while attempts <= 5:
    time.sleep(delay)
    connection_status = input('Connection status (ok/fail): ')

    if connection_status == 'ok':
        break
    
    elif connection_status == 'fail':
        delay *= 2
        attempts += 1
        continue

    attempts += 1

else:
    print('Server Unreachable')