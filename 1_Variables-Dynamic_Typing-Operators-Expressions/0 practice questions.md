Basic Level (Focus: Syntax, Type Checking, and Core Operators):

1. You are initializing a patient's vital signs in a hospital management system. Create variables for temperature (float) and heart_rate (integer). Write the code to verify their data types dynamically using the type() function.

2. For an e-commerce website with a "Desi-Earth" theme, you need a default hex color code. Assign the string "#8B5A2B" to three separate variables (primary_color, button_color, footer_color) in a single line. Then, write an expression to check if primary_color and button_color point to the exact same memory location.

3. Calculate the total fare for a ride-hailing app. The base fare is 50, the per-km rate is 12, and the distance is 8.5 km. Store the result in a total_fare variable and round it down to the nearest whole integer using only arithmetic operators (no imported math modules).

#4. You are generating AI content and have a boolean variable is_premium_user and an integer daily_generation_limit = 10. Write a single mathematical expression that doubles the limit only if is_premium is True, leveraging the fact that booleans evaluate to integers in Python.

5. Given two variables representing user IDs retrieved from a Supabase database, user_id_1 = "uuid-1234" and user_id_2 = "uuid-1234", write one expression to check if their values are equal, and another expression to check if they are the exact same object in memory.

#6. In a music production script, a beat drops every 16 bars. Given a variable current_bar, write an expression using the modulo operator to evaluate to 0 whenever a beat should drop.

7. A FastAPI server has an available memory of 1024 MB. A background task requires 128 MB. Use the correct assignment operator to subtract and update the available memory variable in one step.

8. A user submits a search query via an API. Write an expression using isinstance() to verify that the search_query variable is strictly a string before processing it.

9. In a ride-hailing backend, a driver is considered dispatchable if is_online is True and on_trip is False. Write the logical expression to represent this dispatchable status.

(10). You have a base configuration value of 2 (binary 0010). Use a bitwise left shift operator to quickly multiply this value by 8 to set a new system permission level.








Intermediate Level (Focus: Short-Circuiting, Bitwise Logic, Identity vs. Equality):

11. An e-commerce cart calculation applies a discount. Write an expression using short-circuit logical operators (and / or) that assigns the value 0.10 to a variable discount_rate if coupon_applied is True, and assigns 0.0 if it is False. (Do not use if-else).

12. You are managing authentication lists. token_a = [1, 2, 3] and token_b = [1, 2, 3]. Write code demonstrating why token_a == token_b evaluates to True, but token_a is token_b evaluates to False.

(13). A basic cryptography hashing function requires XORing a user's pin (1234) with a secret backend salt (5678). Write the expression to compute this bitwise XOR and store the ciphertext.

(14). A hospital management system tracks patient privacy preferences using flags: FLAG_ANONYMOUS = 1 (0001) and FLAG_NO_PROMO = 2 (0010). Use a bitwise operator to create a user_preferences integer that holds both flags simultaneously.

(15). Following the previous question, write an expression using the bitwise AND operator to verify if a given user_preferences integer contains the FLAG_NO_PROMO bit.

(16). A background task calculates the size of a file upload. Given file_size_bytes = 1048576, use the bitwise right shift operator to convert this value directly into Megabytes (shifting by 20 bits).

17. You need to connect to a database. You have a variable server_running. Use short-circuit evaluation to execute a function call connect_database() only if server_running is True, without using any if statements.

(18). In Web3, smart contract states often use bitwise inversion. Given an 8-bit permission mask mask = 0b10101010, apply the bitwise NOT operator (~) and explain in a comment why the result appears as a negative integer in Python.

19. Calculate the division of a server's uptime (e.g., uptime_hours = 45) by 24 to get the days and remaining hours. Store the quotient and the remainder in two separate variables using the floor division (//) and modulo (%) operators.

20. You have a string variable user_input. Ensure that a final_username variable defaults to "Guest" if user_input is empty, utilizing the or operator's truthiness short-circuit behavior.







Advanced Level (Focus: Memory Architecture, Bit Masking, Advanced Logic):


21. In Python, small integers are cached by the interpreter. Assign a = 256 and b = 256, then x = 257 and y = 257. Write the expressions to compare a is b, and x is y. In a comment, explain why the identity operator yields different results and what this means for backend memory optimization.

(22). You are building a decentralized Web3 application where transaction signatures are heavily compressed. Extract the lower 4 bits of an integer payload = 205 (binary 11001101) using a bitwise mask and the AND operator.

(23). To optimize a data-processing script for an AI tool, swap the values of two variables, feature_x and feature_y, without using a temporary third variable. Do this first using Python's tuple unpacking, and then write a separate solution using only bitwise XOR operations.

(24). A backend caching system generates a unique key by combining an endpoint ID (e.g., 15) and a user ID (e.g., 1024). Use a bitwise left shift on the endpoint ID by 16 bits, then use bitwise OR with the user ID to pack them into a single integer cache_key.

(25). Given the cache_key integer from the previous question, write the expressions using the bitwise right shift and bitwise AND (with a hexadecimal mask) to unpack and retrieve the original endpoint ID and user ID.

26. You are validating JSON payloads for a strict FastAPI endpoint. Write a single expression that verifies a payload variable is exactly a standard dictionary (and not a custom subclass of a dictionary) by checking its type directly against type({}) instead of using isinstance().

#27. In a ride-hailing app's surge pricing algorithm, demand_multiplier is calculated as active_users / available_drivers. Write an expression that safely computes this, but assigns 1.0 if available_drivers is 0, using strictly logical short-circuiting (and / or) to prevent a ZeroDivisionError.

28. Create a variable secret_key pointing to a list [1, 2, 3]. Assign backup_key = secret_key. Modify the first element of backup_key. Evaluate the identity (is) and equality (==) of the two variables. In a comment, explain the security implications of variable mutability when handling data references in a backend system.

(29). A low-level audio processing algorithm handles values as integers. Use the bitwise NOT (~) and addition to calculate the two's complement (mathematical negation) of an audio sample value sample = 45, mimicking how system architectures handle negative numbers.

30. You are chaining multiple validation checks for a login endpoint: is_valid_email(), is_rate_limited(), and check_password(). Construct a single, unbroken logical expression where check_password() is never executed if the email is invalid or if the user is rate-limited, relying entirely on Python's left-to-right short-circuit sequence.