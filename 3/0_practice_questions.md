Basic Level (Focus: Syntax, range(), basic while loops, and simple control flow):


1. You need to generate sequential order IDs for a Hooka and Ghosa e-commerce database. Write a for loop using range() to print the order numbers from 1001 to 1010.

2. In a ride-hailing app, a countdown timer is displayed to the user while waiting for a cab. Write a while loop that starts at 5, prints the current minute, and decrements by 1 until it reaches 0.

3. A Hospital Management System needs to record the temperatures of exactly 3 patients. Write a for loop that uses the input() function three times to ask for a temperature, and prints "Recorded" after each entry.

4. You are parsing a promo code string: promo = "FESTIVAL26". Write a for loop to iterate through this string and print each character on a new line.

5. A backend service processes a tuple of HTTP status codes: (200, 201, 404, 500, 200). Write a for loop to iterate through them. If the code is 404 or 500, use the continue statement to skip processing it and move to the next code.

6. You are building an admin panel login. Write an infinite while True loop that repeatedly asks for a password using input(). If the password is "admin123", use break to exit the loop and print "Access Granted".

7. Write a for loop that runs 5 times using range(5). Inside the loop, you are planning to write a complex driver-matching algorithm later. For now, use the pass statement to ensure the loop runs without throwing an IndentationError.

8. Python has a unique for...else construct perfect for searching. Write a for loop that iterates through the string "DATABASE". If it finds the letter "X", it should break. If the loop finishes without finding "X" (meaning it never broke), the else block should print "Clean data".

9. Calculate total daily revenue for your Hooka and Ghosa site. Create a variable total = 0. Write a for loop that runs 3 times. Inside, use input() to ask for the revenue of an order, convert it to an integer, and add it to the total. Print the final total.

10. Write an infinite while True loop simulating a server listening for requests. Use input("Enter command: "). If the command is "SHUTDOWN", break the loop and print "Server stopping...".






Intermediate Level (Focus: Nested loops, the else clause, rate limiting, and batch processing):


11. A driver in your ride-hailing app has a daily earnings goal of 500 Rs. Write a while loop that continues to ask for a ride_fare via input() and adds it to their total earnings. The loop should stop automatically as soon as the total earnings are greater than or equal to 500.

12. You have a tuple of patient triage statuses: ("Stable", "Stable", "Critical", "Stable"). Use a for loop to search through them. If "Critical" is found, break and print "Emergency Alert". Use the else clause to print "All patients stable" if no critical status is found.

13. E-commerce product variations: You have a tuple of Hooka sizes ("Small", "Large") and a tuple of flavors ("Mint", "Apple"). Write a nested for loop (one inside the other) to print all possible product combinations (e.g., "Small Mint").

14. Simulate an API rate limiter. Use a for loop to give a user exactly 3 attempts to enter a correct API key via input(). If they guess "SECRET99", break and print "Authenticated". If they fail all 3 attempts, use the for...else clause to print "Account Locked".

15. Grid search for a map feature. Write a nested for loop where x ranges from 0 to 2 and y ranges from 0 to 2. If the coordinate is exactly x=1 and y=1 (representing a blocked road), use continue to skip printing that specific coordinate.

16. Write a while loop to calculate the mathematical factorial of a number provided via input(). (e.g., if the user enters 5, calculate 5 * 4 * 3 * 2 * 1).

17. You are writing a parser for a Hospital Management System that reads HL7-like messages from a tuple: ("ADMIT", "", "TRANSFER", "DISCHARGE"). Use a for loop to process them. If the string is empty "", use continue to skip it.

18. You are pinging driver locations at specific intervals to save battery. Write a for loop using range() with a step argument to print the minute marks: 0, 5, 10, 15, 20, 25, 30.

19. A simple command dispatcher: Write a while True loop that takes input(). If the input is empty, use pass (do nothing and prompt again). If it is "exit", break. Otherwise, print "Processing command".

20. Password validation script: Take a string password = "pass123". Use a for loop to check each character. If a character is a space " ", break immediately and print "Invalid format". Use else to print "Valid format" if no spaces are found.





Advanced Level (Focus: Simulating state machines, retry algorithms, optimization, and system design):


21. Exponential Backoff Algorithm: This is a crucial backend concept for database connections. Write a while loop that attempts to connect 5 times. Start with a delay = 1 second. Inside the loop, ask for input("Connection status (ok/fail): "). If "ok", break. If "fail", multiply the delay by 2 and continue. If all 5 attempts fail, use the else clause to print "Server unreachable".

22. Data Pagination Simulation: You have 15 product IDs in an e-commerce database. Instead of a list, just use range(1, 16). Write an outer while True loop that asks the user input("Press Enter for next page, or type 'quit': "). Inside, use an inner for loop to print exactly 5 items per page. (Hint: you will need to track the current index variable manually).

23. Finding the Minimum: You receive a tuple of nearby cab distances: (12, 8, 15, 3, 9). Without using the built-in min() function, write a for loop that iterates through the tuple and continually updates a shortest_distance variable to find the smallest number.

24. Batch Processing: Your backend needs to process 100 data rows using range(1, 101). However, to prevent memory overflow, you must trigger a garbage collection cycle every 20 rows. Write a for loop that iterates through the 100 rows, and uses the modulo operator (%) to print "Clearing memory..." exactly on rows 20, 40, 60, 80, and 100.

25. Cryptographic Prime Checker: A backend security module needs to verify if a number is prime to generate keys. Ask for an integer via input(). Use a for loop from 2 up to number // 2. If the number is evenly divisible by the loop variable, break (it's not prime). Use the else clause to confidently declare it a prime number.

26. State Machine: Simulate the lifecycle of a ride request. Create a variable state = "SEARCHING". Write a while True loop. Inside, use a match/case block based on state.

    If SEARCHING, wait for input("Found driver? (y/n): "), if 'y', change state to "ARRIVED".

    If ARRIVED, wait for input("Start trip? (y/n): "), change to "IN_TRANSIT".

    If IN_TRANSIT, wait for input("End trip? (y/n): "), change to "COMPLETED".

    If COMPLETED, break the loop.


27. String Parsing without Split: You receive a raw string of comma-separated patient IDs from a legacy system: "101,102,103,". Write a for loop to iterate through every character. Append characters to a temporary current_id string. When you encounter a comma ",", print the current_id, reset it to empty, and continue.

28. Brute Force Defense: You know a secret admin PIN is exactly 3 digits. Write a for loop using range(1000) to guess the pin. Take the "actual pin" via input() before the loop starts. Stop the loop when the guess matches the actual pin, and print exactly how many attempts it took.

29. Load Balancer Routing: Use a while True loop. Take input("Incoming request to (API/WEB/DB) or STOP: "). Use continue if the input is "DB" (refusing direct database access). Use break if it is "STOP". Otherwise, print "Routing to [input]".

30. Two-Pointer Simulation: You have a tuple of sorted integers (1, 2, 3, 4, 5, 6). Use a while loop with two manual index variables: left_index = 0 and right_index = 5. In each iteration, print the values at both indexes, increment left_index by 1, and decrement right_index by 1. Stop the loop when left_index is greater than or equal to right_index.