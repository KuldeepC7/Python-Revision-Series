# 1. You need to generate sequential order IDs for a Hooka and Ghosa e-commerce database. Write a for loop using range() to print the order numbers from 1001 to 1010.
for order_id in range(1001, 1011):
    print(order_id)









# 2. In a ride-hailing app, a countdown timer is displayed to the user while waiting for a cab. Write a while loop that starts at 5, prints the current minute, and decrements by 1 until it reaches 0.

import time

minutes = 5
while minutes != 0:
    print(minutes)
    time.sleep(60)
    minutes -= 1








# 3. A Hospital Management System needs to record the temperatures of exactly 3 patients. Write a for loop that uses the input() function three times to ask for a temperature, and prints "Recorded" after each entry.

for patient in range(1, 4):
    temperature = float(input(f"Enter temperature for patient {patient}: "))
    print(f"Temperature recorded for patient {patient}: {temperature}")












# 4. You are parsing a promo code string: promo = "FESTIVAL26". Write a for loop to iterate through this string and print each character on a new line.

promo = 'FESTIVAL26'

for character in promo:
    print(character)










# 5. A backend service processes a tuple of HTTP status codes: (200, 201, 404, 500, 200). Write a for loop to iterate through them. If the code is 404 or 500, use the continue statement to skip processing it and move to the next code.

http_status_codes = (200, 201, 404, 500, 200)

for status_code in http_status_codes:
    if status_code == 404 or status_code == 500:
        continue
    else:
        print(f"{status_code}: Success")











# 6. You are building an admin panel login. Write an infinite while True loop that repeatedly asks for a password using input(). If the password is "admin123", use break to exit the loop and print "Access Granted".

pas = 'admin123'

while True:
    password = input("Enter admin password: ")
    
    if password == pas:
        print('Correct password :)')
        break
    else:
        print('Wrong password, try again!')
        










# 7. Write a for loop that runs 5 times using range(5). Inside the loop, you are planning to write a complex driver-matching algorithm later. For now, use the pass statement to ensure the loop runs without throwing an IndentationError.

for i in range(5):
    pass









# 8. Python has a unique for...else construct perfect for searching. Write a for loop that iterates through the string "DATABASE". If it finds the letter "X", it should break. If the loop finishes without finding "X" (meaning it never broke), the else block should print "Clean data".

db = 'DATABASE'

for character in db:
    if character == 'X':
        break

    print(character)

else:
    print('Clean data')














# 9. Calculate total daily revenue for your Hooka and Ghosa site. Create a variable total = 0. Write a for loop that runs 3 times. Inside, use input() to ask for the revenue of an order, convert it to an integer, and add it to the total. Print the final total.

total = 0
for i in range(3):
    revenue_of_order = int(input('What is revenue of current order: '))
    total += revenue_of_order

print(total)














# 10. Write an infinite while True loop simulating a server listening for requests. Use input("Enter command: "). If the command is "SHUTDOWN", break the loop and print "Server stopping...".

while True:
    command = input('Enter command: ')

    if command == 'SHUTDOWN':
        print('Server stopping.....')
        break













# 11. A driver in your ride-hailing app has a daily earnings goal of 500 Rs. Write a while loop that continues to ask for a ride_fare via input() and adds it to their total earnings. The loop should stop automatically as soon as the total earnings are greater than or equal to 500.

daily_earning_goal = 500
riders_earning_today = 0

while daily_earning_goal >= riders_earning_today:
    ride_fare = float(input('Enter current ride fare: '))
    riders_earning_today += ride_fare

print(riders_earning_today)














# 12. You have a tuple of patient triage statuses: ("Stable", "Stable", "Critical", "Stable"). Use a for loop to search through them. If "Critical" is found, break and print "Emergency Alert". Use the else clause to print "All patients stable" if no critical status is found.

patient_triage_statuses = ('Stable', 'Stable', 'Critical', 'Stable')

for status in patient_triage_statuses:
    if status == 'Critical':
        print('Emergency Alert')
        break
    
    else:
        print('All patients stable')









    
# 13. E-commerce product variations: You have a tuple of Hooka sizes ("Small", "Large") and a tuple of flavors ("Mint", "Apple"). Write a nested for loop (one inside the other) to print all possible product combinations (e.g., "Small Mint").

hooka_size = ('Small', 'Large')
flavors = ('Mint', 'Apple')

for size in hooka_size:
    for flavor in flavors:
        print(size, flavor)













# 14. Simulate an API rate limiter. Use a for loop to give a user exactly 3 attempts to enter a correct API key via input(). If they guess "SECRET99", break and print "Authenticated". If they fail all 3 attempts, use the for...else clause to print "Account Locked".

api = 'SECRET99'

for i in range(0, 3):
    api_key = input('Enter API key: ')
    if api_key == api:
        print('Authenticated')
        break

else:
    print('Account Locked')











# 15. Grid search for a map feature. Write a nested for loop where x ranges from 0 to 2 and y ranges from 0 to 2. If the coordinate is exactly x=1 and y=1 (representing a blocked road), use continue to skip printing that specific coordinate.

for x in range(3):
    for y in range(3):
        if x == 1 and y == 1:
            continue
        else:
            print(x, y)











# 16. Write a while loop to calculate the mathematical factorial of a number provided via input(). (e.g., if the user enters 5, calculate 5 * 4 * 3 * 2 * 1).

number = int(input('Enter the number of which you want factorial: '))
factorial = 1

while number != 0:
    factorial *= number
    number -= 1

print(factorial)











# 17. You are writing a parser for a Hospital Management System that reads HL7-like messages from a tuple: ("ADMIT", "", "TRANSFER", "DISCHARGE"). Use a for loop to process them. If the string is empty "", use continue to skip it.

message = ('ADMIT', '', 'TRANSFER', 'DISCHARGE')

for status in message:
    if status:
        print(status)
    else:
        continue












# 18. You are pinging driver locations at specific intervals to save battery. Write a for loop using range() with a step argument to print the minute marks: 0, 5, 10, 15, 20, 25, 30.

import time

for i in range(0, 31, 5):
    print(i)
    time.sleep(5 * 60)














# 19. A simple command dispatcher: Write a while True loop that takes input(). If the input is empty, use pass (do nothing and prompt again). If it is "exit", break. Otherwise, print "Processing command".

while True:
    command = input('Enter your command: ')

    if command == '':
        pass

    elif command == 'exit':
        break

    else:
        print('Processing command')






    






# 20. Password validation script: Take a string password = "pass123". Use a for loop to check each character. If a character is a space " ", break immediately and print "Invalid format". Use else to print "Valid format" if no spaces are found.

password = 'pass123'

for character in password:
    if character == ' ':
        print('Invalid format!')
        break
else:
    print('Valid format')
















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


















# 22. Data Pagination Simulation: You have 15 product IDs in an e-commerce database. Instead of a list, just use range(1, 16). Write an outer while True loop that asks the user input("Press Enter for next page, or type 'quit': "). Inside, use an inner for loop to print exactly 5 items per page. (Hint: you will need to track the current index variable manually).


# items = ['something', 'one', 'two', 'three', 'four']

index_variable = 3
pagination_variable = 1

while True:
    if index_variable == 0:
        break

    else: 
        command = input('Press enter for next page, or type "quit": ')
        if command == 'quit':
            break

        elif command == '':
            for i in range (pagination_variable, pagination_variable + 5):
                print(f'Product {i} with product id: {i}')
            
            pagination_variable += 5
            index_variable -= 1
        
        else:
            print('Enter correct command!')















# 23. Finding the Minimum: You receive a tuple of nearby cab distances: (12, 8, 15, 3, 9). Without using the built-in min() function, write a for loop that iterates through the tuple and continually updates a shortest_distance variable to find the smallest number.

nearby_cab_distances = (12, 8, 15, 3, 9)

shortest_distance = 0

for distance in nearby_cab_distances:
    if nearby_cab_distances[0] == distance:
        shortest_distance = distance
    
    else:
        if shortest_distance > distance:
            shortest_distance = distance

print(shortest_distance)

















# 24. Batch Processing: Your backend needs to process 100 data rows using range(1, 101). However, to prevent memory overflow, you must trigger a garbage collection cycle every 20 rows. Write a for loop that iterates through the 100 rows, and uses the modulo operator (%) to print "Clearing memory..." exactly on rows 20, 40, 60, 80, and 100.

for row in range(1, 101):
    # print(row)
    # if row % 20 == 0:
    #     print("Clearing memory.....")
    if row % 20 != 0:
        print(row)
    
    else:
        print("Clearing memory.....")











# 25. Cryptographic Prime Checker: A backend security module needs to verify if a number is prime to generate keys. Ask for an integer via input(). Use a for loop from 2 up to number // 2. If the number is evenly divisible by the loop variable, break (it's not prime). Use the else clause to confidently declare it a prime number.

number = int(input('Enter a number: '))

for i in range(2, number // 2):
    if (number % i == 0):
        print('Not a prime number!')
        break

else:
    print('Prime number :)')












# 26. State Machine: Simulate the lifecycle of a ride request. Create a variable state = "SEARCHING". Write a while True loop. Inside, use a match/case block based on state.
#     If SEARCHING, wait for input("Found driver? (y/n): "), if 'y', change state to "ARRIVED".
#     If ARRIVED, wait for input("Start trip? (y/n): "), change to "IN_TRANSIT".
#     If IN_TRANSIT, wait for input("End trip? (y/n): "), change to "COMPLETED".
#     If COMPLETED, break the loop.

state = 'SEARCHING'

while True:
    match state:
        case 'SEARCHING':
            driver_found = input('Found driver? (y/n): ')
            if driver_found == 'y':
                state = 'ARRIVED'
        
        case 'ARRIVED':
            trip_start = input('Start trip? (y/n): ')
            if trip_start == 'y':
                state = 'IN_TRANSIT'
            
        case 'IN_TRANSIT':
            trip_end = input('End trip? (y/n): ')
            if trip_end == 'y':
                state = 'COMPLETED'
        
        case 'COMPLETED':
            print('Trip Completed :)')
            break














# 27. String Parsing without Split: You receive a raw string of comma-separated patient IDs from a legacy system: "101,102,103,". Write a for loop to iterate through every character. Append characters to a temporary current_id string. When you encounter a comma ",", print the current_id, reset it to empty, and continue.

patient_ids = '101,102,103,'
current_id = ''

for character in patient_ids:
    if character == ',':
        print(current_id)
        current_id = ''
    else:
        current_id += character















# 28. Brute Force Defense: You know a secret admin PIN is exactly 3 digits. Write a for loop using range(1000) to guess the pin. Take the "actual pin" via input() before the loop starts. Stop the loop when the guess matches the actual pin, and print exactly how many attempts it took.

PIN = int(input('Enter your admin pin: '))

for guess in range(1000):
    if guess == PIN:
        print(guess)












# 29. Load Balancer Routing: Use a while True loop. Take input("Incoming request to (API/WEB/DB) or STOP: "). Use continue if the input is "DB" (refusing direct database access). Use break if it is "STOP". Otherwise, print "Routing to [input]".


while True:
    request = input('Incoming request to (API/WEB/DB) or STOP: ')
    
    if request == 'DB':
        continue
    elif request == 'STOP':
        break
    else:
        print(f'Routng to {request}')






# 30. Two-Pointer Simulation: You have a tuple of sorted integers (1, 2, 3, 4, 5, 6). Use a while loop with two manual index variables: left_index = 0 and right_index = 5. In each iteration, print the values at both indexes, increment left_index by 1, and decrement right_index by 1. Stop the loop when left_index is greater than or equal to right_index.

sorted_integers = (1, 2, 3, 4, 5, 6)

left_index = 0
right_index = 5

while left_index <= right_index:
    print(f'values: {left_index} and {right_index}')
    
    left_index += 1
    right_index -= 1