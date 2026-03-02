# 1. You are initializing a patient's vital signs in a hospital management system.
#Create variables for temperature (float) and heart_rate (integer).
#Write the code to verify their data types dynamically using the type() function.


temperature = 25.7
heart_rate = 75


print(type(temperature))
print(type(heart_rate))






#2. For an e-commerce website with a "Desi-Earth" theme, you need a default hex color code.
#Assign the string "#8B5A2B" to three separate variables (primary_color, button_color, footer_color) in a single line.
#Then, write an expression to check if primary_color and button_color point to the exact same memory location.


primary_color = button_color = footer_color = "#8B5A2B"

print(id(primary_color)) #1518769604144
print(id(button_color))#2093971932720 2093971932720

print(id(primary_color) == id(button_color))






# 3. Calculate the total fare for a ride-hailing app. The base fare is 50, the per-km rate is 12, and the distance is 8.5 km. Store the result in a total_fare variable and round it down to the nearest whole integer using only arithmetic operators (no imported math modules).

base_fare = 50
rate_per_km = 12
distance = 8.5

total_fare = base_fare + (rate_per_km * distance)

print(int(total_fare))






# 4. You are generating AI content and have a boolean variable is_premium_user and an integer daily_generation_limit = 10. Write a single mathematical expression that doubles the limit only if is_premium is True, leveraging the fact that booleans evaluate to integers in Python.

is_premium_user = True
daily_generation_limit = 0

daily_generation_limit = (is_premium_user > 0) * 20 + (is_premium_user <= 0) * 10 #How this line is working, explain me

print(daily_generation_limit)







# 5. Given two variables representing user IDs retrieved from a Supabase database, user_id_1 = "uuid-1234" and user_id_2 = "uuid-1234", write one expression to check if their values are equal, and another expression to check if they are the exact same object in memory.

user_id_1 = 'uuid-1234'
user_id_2 = 'uuid-1234'

print(user_id_1 == user_id_2)
print(id(user_id_1) == id(user_id_2))
print(id(user_id_1))
print(id(user_id_2))







# 6. In a music production script, a beat drops every 16 bars. Given a variable current_bar, write an expression using the modulo operator to evaluate to 0 whenever a beat should drop.

current_bar = 48

will_drop = (current_bar % 16 == 0)

print(will_drop)






# 7. A FastAPI server has an available memory of 1024 MB. A background task requires 128 MB. Use the correct assignment operator to subtract and update the available memory variable in one step.

available_memory = 1024

print(available_memory)

background_tasks_memory_requirement = 128

available_memory = available_memory - background_tasks_memory_requirement

print(available_memory)








# 8. A user submits a search query via an API. Write an expression using isinstance() to verify that the search_query variable is strictly a string before processing it.

search_query = "Hello World"

print(isinstance(search_query, str))









# 9. In a ride-hailing backend, a driver is considered dispatchable if is_online is True and on_trip is False. Write the logical expression to represent this dispatchable status.

is_online = True
on_trip = False
print("Driver is dispatchable")








# 10. You have a base configuration value of 2 (binary 0010). Use a bitwise left shift operator to quickly multiply this value by 8 to set a new system permission level.


base_configuration_value = 2
new_system_permission = 2 << 8
print(new_system_permission)









# 11. An e-commerce cart calculation applies a discount. Write an expression using short-circuit logical operators (and / or) that assigns the value 0.10 to a variable discount_rate if coupon_applied is True, and assigns 0.0 if it is False. (Do not use if-else).

discount_rate = 0

coupan_applied = False

discount_rate = (coupan_applied > 0) * 0.10 or (coupan_applied <= 0) * 0.0

print(discount_rate)











# 12. You are managing authentication lists. token_a = [1, 2, 3] and token_b = [1, 2, 3]. Write code demonstrating why token_a == token_b evaluates to True, but token_a is token_b evaluates to False.


#Explain me this program, why the results are different
token_a = [1,2,3]
token_b = [1,2,3]

a = 5
b = 5

print(token_a == token_b) # checks whether the value is same or not of both the lists

print(token_a is token_b) # Checks whether are they holds same memory address or not, compare their memory address. And list is mutable and stores ts elements in adjacent memory addresses, but two lists with the same value and elements are stored in different memory address.

print(id(token_a) == id(token_b)) 











# 13. A basic cryptography hashing function requires XORing a user's pin (1234) with a secret backend salt (5678). Write the expression to compute this bitwise XOR and store the ciphertext.


user_pin = 1234
secret_backend_salt = 5678

ciphertext = user_pin ^ secret_backend_salt
print(ciphertext)









# 14. A hospital management system tracks patient privacy preferences using flags: FLAG_ANONYMOUS = 1 (0001) and FLAG_NO_PROMO = 2 (0010). Use a bitwise operator to create a user_preferences integer that holds both flags simultaneously.

FLAG_ANONYMOUS = 1
FLAG_NO_PROMO = 2

user_preferences = FLAG_ANONYMOUS | FLAG_NO_PROMO
print(user_preferences)
print(FLAG_ANONYMOUS == user_preferences & FLAG_ANONYMOUS)










# 15. Following the previous question, write an expression using the bitwise AND operator to verify if a given user_preferences integer contains the FLAG_NO_PROMO bit.

FLAG_ANONYMOUS = 1
FLAG_NO_PROMO = 2

user_preferences = FLAG_ANONYMOUS | FLAG_NO_PROMO
print(FLAG_ANONYMOUS == user_preferences & FLAG_ANONYMOUS)








# 16. A background task calculates the size of a file upload. Given file_size_bytes = 1048576, use the bitwise right shift operator to convert this value directly into Megabytes (shifting by 20 bits).


file_size_bytes = 1048576
file_size_megabytes = file_size_bytes >> 20
print(file_size_megabytes)










# 17. You need to connect to a database. You have a variable server_running. Use short-circuit evaluation to execute a function call connect_database() only if server_running is True, without using any if statements.

def connect_database():
    pass


server_running = True

# Explain me how this works
print(server_running > 0 and connect_database())











# 18. In Web3, smart contract states often use bitwise inversion. Given an 8-bit permission mask mask = 0b10101010, apply the bitwise NOT operator (~) and explain in a comment why the result appears as a negative integer in Python.

mask = 0b10101010
inversion_mask = ~mask
print(inversion_mask)

# I dont knwo why this happens please explain me this in very easy way









# 19. Calculate the division of a server's uptime (e.g., uptime_hours = 45) by 24 to get the days and remaining hours. Store the quotient and the remainder in two separate variables using the floor division (//) and modulo (%) operators.


uptime_hours = 45

remaining_days = uptime_hours / 24

remaining_hours = uptime_hours % 24

print("Remaining days for server uptime", remaining_days)
print("Remaining hours for server uptime", remaining_hours)









# 20. You have a string variable user_input. Ensure that a final_username variable defaults to "Guest" if user_input is empty, utilizing the or operator's truthiness short-circuit behavior.


user_input = 'Kuldeep'

# Explain me how this is happening
user_input = (user_input != '') * user_input or (user_input == '') * 'Guest'

print(user_input)











# 21. In Python, small integers are cached by the interpreter. Assign a = 256 and b = 256, then x = 257 and y = 257. Write the expressions to compare a is b, and x is y. In a comment, explain why the identity operator yields different results and what this means for backend memory optimization.


a = 256
b = 256
x = 257
y = 257

print(a is b)
print(x is y)

'''
The python interpreter holds a variable's value in memory with a particular address. And it doesn't create a new memory address to store the same value, like if we created a variable a with value 256, then it holds this 256 value with a particular memory address. And when create another variable lets say b with the same value 256, then the interpreter will points b variable to also the same memory address of a variable. And when identity operator checks whether they are in same memory address and have similar values or not, it found that they both have same value and points to the same memory address.

This is beneficial in memory optimization of backend because, for different variable objects with same value, all variables points to the same memory address and it will use less memory. There will be less memory consumption.  
'''


















# 22. You are building a decentralized Web3 application where transaction signatures are heavily compressed. Extract the lower 4 bits of an integer payload = 205 (binary 11001101) using a bitwise mask and the AND operator.

# I dont know how to do it











# 23. To optimize a data-processing script for an AI tool, swap the values of two variables, feature_x and feature_y, without using a temporary third variable. Do this first using Python's tuple unpacking, and then write a separate solution using only bitwise XOR operations.

feature_x = 5
feature_y = 7

# data = (feature_x, feature_y)
# feature_y, feature_x = data

# print(feature_x)
# print(feature_y)

feature_x = feature_x | feature_y
feature_y = feature_x ^ feature_y
feature_x = feature_x ^ feature_y

print(feature_x)
print(feature_y)














# 24. A backend caching system generates a unique key by combining an endpoint ID (e.g., 15) and a user ID (e.g., 1024). Use a bitwise left shift on the endpoint ID by 16 bits, then use bitwise OR with the user ID to pack them into a single integer cache_key.


endpoint_ID = 15
user_ID = 1024

cache_key = (endpoint_ID << 16) | user_ID
print(cache_key)











# 25. Given the cache_key integer from the previous question, write the expressions using the bitwise right shift and bitwise AND (with a hexadecimal mask) to unpack and retrieve the original endpoint ID and user ID.

endpoint_ID = 15
user_ID = 1024

# cache_key = (endpoint_ID << 16) | user_ID
# print(cache_key)


cache_key = 984064
# dont know how to do it












# 26. You are validating JSON payloads for a strict FastAPI endpoint. Write a single expression that verifies a payload variable is exactly a standard dictionary (and not a custom subclass of a dictionary) by checking its type directly against type({}) instead of using isinstance().

json_payload = {
    'a': {}
}

dictionary_or_not = (type(json_payload) == type({}))
print(dictionary_or_not)
















# 27. In a ride-hailing app's surge pricing algorithm, demand_multiplier is calculated as active_users / available_drivers. Write an expression that safely computes this, but assigns 1.0 if available_drivers is 0, using strictly logical short-circuiting (and / or) to prevent a ZeroDivisionError.

active_users = 5
available_drivers = 1
demand_multiplier = (available_drivers == 0) * 1.0 + (available_drivers > 0) * active_users/available_drivers

print(demand_multiplier)


















# 28. Create a variable secret_key pointing to a list [1, 2, 3]. Assign backup_key = secret_key. Modify the first element of backup_key. Evaluate the identity (is) and equality (==) of the two variables. In a comment, explain the security implications of variable mutability when handling data references in a backend system.

secret_key = [1, 2, 3]
backup_key = secret_key
backup_key[0] = 5

print(secret_key)
print(backup_key)

print(secret_key == backup_key)
print(backup_key is secret_key)

'''
The security implications of variable mutability when handling data references in a backend system:
- So here data references means that the secret_key and its value is a refernce for the backup_key. And the backup key is referencing to the same memory address and value that of the secret_key.

- So when we change/update/add/delete any element of any one of the data objects/lists, then it will change that value in memory address (which is shared by both) directly. Hence the other data object/list will be also get affected.

- In this case we are changing the first element of backup_key, and both (secret_key and backup_key) has the same memory address, so it will change the first element in that shared memory address. And the first element of secret_key will also get change in this case.

- Now in real backend system, it will cause issue by breaking the working functionality of secret_key, when it get modified. So we never have to make any backup of anything in backend by direct referencing it to the main working variable or any data object. And if we modify the data in backup object, it will also change in the main working data object.

'''

















# 29. A low-level audio processing algorithm handles values as integers. Use the bitwise NOT (~) and addition to calculate the two's complement (mathematical negation) of an audio sample value sample = 45, mimicking how system architectures handle negative numbers.


sample = 45
# dont know how to do it



















# 30. You are chaining multiple validation checks for a login endpoint: is_valid_email(), is_rate_limited(), and check_password(). Construct a single, unbroken logical expression where check_password() is never executed if the email is invalid or if the user is rate-limited, relying entirely on Python's left-to-right short-circuit sequence.

def is_valid_email():
    return True    

def is_rate_limited():
    return True

def check_password():
    return True

l_to_r = (check_password() and (is_valid_email() and is_rate_limited))

print(l_to_r) 