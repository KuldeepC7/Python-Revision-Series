# 1. You are writing the triage logic for a hospital management system. Given a variable patient_temperature, write an if/elif/else block that assigns a status variable to "Critical" if the temperature is above 103.0, "Fever" if it's above 99.5, and "Normal" otherwise.

patient_temperature = 105.0
pateint_status = ''

if patient_temperature >= 103.0:
    pateint_status = 'Critical'

elif patient_temperature >= 99.5:
    pateint_status = 'Fever'

else:
    pateint_status = 'Normal'

print(pateint_status)












# 2. In a ride-hailing app, a user is trying to book a cab. Write a simple if/else statement that checks if wallet_balance is greater than or equal to estimated_fare. If it is, assign booking_confirmed = True, otherwise assign False.

wallet_balance = 70
estimated_fare = 50

if estimated_fare < wallet_balance:
    booking_confirmed = True
    print(booking_confirmed)

else:
    booking_confirmed = False
    print(booking_confirmed)












# 3. Rewrite the logic from Question 2 using a single Python Ternary operator to assign the boolean value to booking_confirmed in one line.

# value_if_true if condition else value_if_false

wallet_balance = 52
estimated_fare = 55
booking_confirmed = True if estimated_fare < wallet_balance else False

print(booking_confirmed)











# 4. An ed-tech platform ("Coder's Loop") assigns user roles based on a string variable signup_code. Write an if/elif/else block: if the code is "TEACH26", role is "Instructor"; if "LEARN26", role is "Student"; else, role is "Guest".

signup_code = ''

user_role = 'Student' if signup_code=='LEARN26' else ('Instructor' if signup_code=='TEACH26' else 'Guest')

print(user_role)










# 5. A FastAPI endpoint receives an authentication token. Write an if/else block to check if auth_token is an empty string. If it is empty, assign http_status = 401. Else, assign http_status = 200.

auth_token = 'fsh4r29i0wr90hjsfbf84wurjfsbefb'
http_status = 200 if auth_token != '' else 401
print(http_status)












# 6. You are checking the health status of a cloud-native Heroku deployment. The server_status variable can be "GREEN", "YELLOW", or "RED". Write a basic match/case block to assign an action string: "All good" for GREEN, "Check logs" for YELLOW, and "Restart Dyno" for RED.

server_status = 'RED'
action = ''

match server_status:
    case 'GREEN':
        action = "All good"
    
    case 'YELLOW':
        action = 'Check logs'
    
    case 'RED':
        action = 'Restart Dyno'


print(action)



















# 7. For a "Desi-Earth" e-commerce checkout, apply a shipping fee. Use a ternary operator to assign shipping_fee = 0 if cart_total > 500, else assign shipping_fee = 50.

cart_total = float(input("Enter cart total: "))

shipping_fee = 0 if cart_total > 500 else 50
print(shipping_fee)













# 8. A hospital ward has an age restriction. Given patient_age, write an if/else block that sets admission_allowed = True only if the age is exactly 18 or older.

patient_age = int(input('Enter patient age: '))

admission_allowed = True if patient_age >= 18 else False
print(admission_allowed)













# 9. An external API returns an HTTP status code as an integer (200, 400, 404, or 500). Write a match/case block that assigns a string response_message based on these exact numbers, and use the wildcard case (_) to assign "Unknown Error" for any other number.

status_code = int(input('Enter status coce: '))
response_message = ''

match status_code:
    case 200:
        response_message = 'success'
    
    case 400: 
        response_message = 'Bad Rquest'

    case 404:
        response_message = 'page not found'

    case 500:
        response_message = 'Internal Server Error'
    
    case _:
        response_message = 'Unknown Error'
    
print(response_message)















# 10. A security module tracks failed_login_attempts. Write an if/else block that sets a boolean account_locked to True if the attempts exceed 5, and False otherwise.

failed_login_attempts = int(input('No. of login attempts: '))

account_locked = True if failed_login_attempts > 5 else False

print(account_locked)
















# 11. An incoming hospital record is represented as a tuple: record = ("symptom", severity_level). For example, ("chest_pain", 8). Write a match/case block that unpacks this tuple. If the symptom is "chest_pain", assign priority 1. If "fever", assign priority 2. Otherwise, assign priority 3.

priority = 0
record = ("Pain in hands", 2)

symptom, severity_level = record

match symptom:
    case "chest pain":
        priority = 1
    
    case "fever":
        priority = 2
    
    case _:
        priority = 3

print(priority)


















# 12. A ride-hailing app needs to classify vehicle types. Given vehicle_type, write a match/case block using the OR (|) pattern. If it's "bike", assign category = "2-wheeler". If it's "mini" or "prime", assign category = "car". Wildcard should assign "unknown".

vehicle_type = input('Vehicle Type: ')
category = ''

match vehicle_type:
    case 'bike':
        category = '2-wheeler'
    
    case 'mini' | 'prime':
        category = 'car'
    
    case _:
        category = 'unknown'

print(category)




















# 13. In your ed-tech platform, determine video streaming quality. Write a nested if/else block: First check if is_premium_user is True. If so, check if bandwidth_mbps >= 10; if true, quality is "4K", else "1080p". If not a premium user, quality is "720p" regardless of bandwidth.

is_premium_user = bool(int(input('Enter 0 for false and 1 for true: ')))
quality = ''

if is_premium_user:
    bandwidth_mbps = int(input('Enter your bandwidth in mbps: '))
    if bandwidth_mbps >= 10:
        quality = '4K'
    else:
        quality = '1080p'
else:
    quality = '720p'

print(quality)

















# 14. Write a nested ternary operator for a system logger. Assign log_level to "DEBUG" if environment == "dev", "INFO" if environment == "prod", and "WARN" for anything else.

# system logger

environment = input('What is environment type: ')

log_level = 'DEBUG' if environment == 'dev' else('INFO' if environment == 'prod' else 'WARN')

print(log_level)

















# 15. A webhook sends deployment events as a tuple: event = ("deploy", branch_name). Write a match/case block that unpacks the tuple, but use an if guard inside the case so that it only sets trigger_build = True if the action is "deploy" AND the branch is "main".



# ste = 'someone, me, 7, x, 4.0'
# tup = tuple(ste.split(','))
# print(tup)

event = ('deploy', 'main')
action, branch = event
trigger_build = None

match action:
    case 'deploy':
        if branch == 'main':
            trigger_build = True
        else:
            trigger_build = False
    
    case _:
        trigger_build = False


print(trigger_build)


















# 16. E-commerce discount logic: Write an if/elif/else block that checks promo_code. If it's "NEW_USER", discount is 20%. If it's "FESTIVAL", discount is 15%. However, a user can only use "NEW_USER" if the boolean is_first_order is True. Ensure this logic is handled correctly.


promo_code = input('Enter your coupan code for discount: ')
discount_percentage = None

if promo_code == 'NEW_USER':
    is_first_order = bool(int(input('Press 1 for true and 0 for false: ')))
    if is_first_order:
        discount_percentage = 20
    
    else:
        discount_percentage = "You're not a new user!"

elif promo_code == 'FESTIVAL':
    discount_percentage = 15

else:
    discount_percentage = 'Wrong promo code or coupan code!'


print(discount_percentage)























# 17. Evaluate a valid ride request without nested ifs. Write a single if statement using logical operators (and, not) that sets ride_accepted = True only if driver_available is True, user_banned is False, and distance_km is less than 50.

user_banned = bool(int(input('Is user banned or not: ')))
driver_available = bool(int(input('Is driver available: ')))
distance_in_km = eval(input('Enter distance in km: '))

ride_accepted = True if (driver_available and not user_banned and (distance_in_km < 50)) else False

# ride_accepted = False
# if not user_banned:
#     driver_available = bool(int(input('Is driver available: ')))
#     if driver_available:
#         distance_in_km = eval(input('Enter distance in km: '))
#         if distance_in_km < 50:
#             ride_accepted = True

print(ride_accepted)






















# 18. Medical records arrive via an HL7-like stream as tuples of varying lengths: ("ADMIT", patient_id) or ("TRANSFER", patient_id, new_ward). Write a match/case block that handles both patterns and extracts the variables appropriately to print a routing message.

record = ('TRANSFER', 1257, "OT")
routing_message = None

match (record[0]):
    case 'ADMIT':
        routing_message = f'Patient with id {record[1]}, needs to be admit'
    
    case 'TRANSFER':
        if len(record) > 2:
            routing_message = f'Pateint with id {record[1]}, needs to be transfer in {record[2]}'
        else:
            routing_message = "NO ward name"

print(routing_message)




















# 19. Password validation backend: Write an if/else structure that first checks if len(password) > 8. If it is, use an inner if/else to check if the string "!" or "@" is present in the password, setting is_strong = True if so.

password = input('Enter password: ')
is_strong = False

if len(password) > 8:
    if '!' or '@' in password:
        is_strong = True

print(is_strong)





















# 20. A script categorizes tech blogs based on a keyword string. Write an if/elif/else block: if the keyword is exactly "solar" or "wind", category is "Renewable". If "battery", category is "Storage". Else, "General".

keyword_in_blog = input('What is keyword: ')
category = None

if keyword_in_blog == 'solar' or keyword_in_blog == 'wind':
    category = 'Renewable'

elif keyword_in_blog == 'battery':
    category = 'Storage'

else:
    category = 'General'

print(category)



















# 21. You are building an API command dispatcher. The payload is a tuple: payload = ("UPDATE", "user", 1024). Write a match/case block that matches this exact 3-item structure, extracts the action, entity, and ID into variables, and handles it. Include a fallback case for malformed tuples.


payload = ('UPDATE', 'user', 1024)

# match len(payload):
#     case 3:
#         if isinstance(payload[0], str) and isinstance(payload[1], str) and isinstance(payload[2], int):
#             action,entity,ID = payload
#             print(action, entity, ID)
#             print(type(action), type(entity), type(ID))
        
#         else: 
#             print('malformed tuple')
    
#     case _:
#         print('malformed tuple')


match payload:
    case (action, entity, ID):
        if isinstance(action, str) and isinstance(entity, str) and isinstance(ID, int):
            print(action, entity, ID)
            print(type(action), type(entity), type(ID))
        else:
            print('Malformed tuple')
    
    case _:
        print('Malformed tuple')






















# 22. A webhook sends live driver coordinates: location_update = (latitude, longitude, status). Write a match/case block to unpack this. Add a guard (if) to the case that triggers an "Out of Bounds Alert" if either latitude or longitude is strictly less than 0.


location_update_str = input('Enter cordinates and status with separation of commas and also between x & y cordinates: ')
location_update_tuple = tuple(location_update_str.split(','))

if len(location_update_tuple) == 3:
    location_update = (int(location_update_tuple[0]), int(location_update_tuple[1]), location_update_tuple[2])
    match location_update:
        case (latitude, longitude, status):
            if (latitude > 0 and longitude > 0):
                print(True, location_update)
            else:
                print(False, "Out of Bounds Alert")
    
        case _:
            print(False, 'Out of Bounds Alert')

else:
    print("Tuple is malformed!")























# 23. Combine a ternary operator with short-circuiting for an on-call system. Assign a final_doctor variable: it should be primary_doctor if primary_available is True, otherwise backup_doctor if backup_available is True, and if neither are available, default to the string "Emergency Ward". Write this in a single line.

primary_available = False
backup_available = False

final_doctor = 'primary_doctor' if primary_available else('backup_doctor' if backup_available else 'Emergency Ward')
print(final_doctor)

















# 24. Cloud infrastructure config parsing: You receive a nested tuple config = ("dyno", ("web", 5)). Write a match/case block that matches this nested structure, extracts the integer 5 into a variable count, and uses a guard to trigger a "Scale Warning" if count > 3.

config = ('dyno', ('web', 5))

match config:
    case (vps_type, (platform, count)):
        if count > 3:
            print('Scale Warning')
        
        else:
            print('Continue')
        
    case _:
        print('Malformed tuple')


















# 25. Design a rudimentary rate-limiting engine. You have a tuple request = (user_tier, request_count). Write a match/case block. If tier is "free" and count < 100, allow. If tier is "pro" and count < 1000, allow. Else, block. Use structural matching with guards.

request = ('free', 75)
allow_or_not = None

user_tier, request_count = request

match user_tier:
    case 'free':
        if request_count < 100:
            allow_or_not = 'allow'
        else:
            allow_or_not = 'block'
    
    case 'pro':
        if request_count < 1000:
            allow_or_not = 'allow'
        else:
            allow_or_not = 'block'
    
    case _:
        allow_or_not = 'block'

print(allow_or_not)























# 26. Course enrollment logic. Using an if/else block, first check if course_capacity > 0. If true, use a ternary operator inside the block to assign status = "Enrolled" if user_credits >= course_cost, otherwise assign "Insufficient Credits".

course_capacity = 2
user_credits = 1000
course_cost = 250
status = None

if course_capacity > 0:
    status = 'Enrolled' if user_credits >= course_cost else 'Insufficient Credits'

else: 
    status = 'Nothing'


print(status)




















# 27. A payment gateway returns varying tuple structures: ("SUCCESS", transaction_id) or ("FAILED", error_code, retry_allowed_boolean). Write a match/case block that handles both. For the failed case, extract the boolean and use a nested if to determine if the system should re-queue the payment.


p_g_r_str = input('Enter tuple elements with comma between them in single line: ')

p_g_r_tuple = tuple(p_g_r_str.split(','))

if len(p_g_r_tuple) < 3:
    payment_gateway_returns = (p_g_r_tuple[0], int(p_g_r_tuple[1]))

else:
    payment_gateway_returns = (p_g_r_tuple[0], int(p_g_r_tuple[1]), eval(p_g_r_tuple[2]))



match payment_gateway_returns:
    case (response_message, transaction_id):
        print('Success', transaction_id)
    
    case (response_message, error_code, retry_allowed_boolean):
        if retry_allowed_boolean:
            print('re-queue: The transaction is in queue again')
        
        else:
            print('Retry')
    
    case _:
        print('Malformed tuple')























# 28. E-commerce inventory check. Given an integer stock_level, write a match/case block. Case 0: assign "Out of stock". Case 1, 2, or 3 (using the OR | operator): assign "Low stock alert". For any other number, use the wildcard _ with a guard (if stock_level > 10) to assign "In stock", and a final wildcard without a guard to assign "Check manually".

stock_level = int(input('What is stock level current: '))
current_stock = None

match stock_level:
    case 0:
        current_stock = 'Out of stock'
    
    case 1 | 2 | 3:
        current_stock = 'Low stock alert'
    
    case _:
        if stock_level > 10:
            current_stock = 'In stock'
        
        else:
            current_stock = 'Check manually'

print(current_stock)























# 29. Build an Access Control List (ACL) router. You have request = (user_role, action). Write a match/case block. "admin" can do anything (match role, ignore action). "editor" can match if action is "read" | "write". "viewer" can match only if action is "read".

request_str = input('Access control request: ')
request = tuple(request_str.split(','))
user_role, action = request

match user_role:
    case 'admin':
        print('can do anything')
    
    case 'editor':
        if action == 'read' or action == 'write':
            print('access granted')
        else:
            print('Not allowed')

    case 'viewer':
        if  action == 'read':
            print('Only reading allowed')
        else: 
            print('request for wrong permission')























# 30. You are designing a custom routing framework from scratch. The incoming request is a string route. Write a match/case block that handles exact matches for "/home" and "/api/v1/users". Add a case that handles anything starting with "/admin" (hint: you can't use string methods like .startswith() inside the case pattern itself, so you must use a wildcard _ with an if guard) and return a 403 Forbidden.


request = input('Route: ')

match request:
    case '/home':
        print('Redirecting to home')
    
    case '/api/v1/users':
        print('Redirecting to users page')
    
    case _:
        if request.startswith('/admin'):
            print('403 Forbidden')
        
        else:
            print('Wrong route')