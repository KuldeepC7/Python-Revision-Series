Basic Level (Focus: Core branching, simple ternaries, and basic matching)


1. You are writing the triage logic for a hospital management system. Given a variable patient_temperature, write an if/elif/else block that assigns a status variable to "Critical" if the temperature is above 103.0, "Fever" if it's above 99.5, and "Normal" otherwise.

2. In a ride-hailing app, a user is trying to book a cab. Write a simple if/else statement that checks if wallet_balance is greater than or equal to estimated_fare. If it is, assign booking_confirmed = True, otherwise assign False.

3. Rewrite the logic from Question 2 using a single Python Ternary operator to assign the boolean value to booking_confirmed in one line.

4. An ed-tech platform ("Coder's Loop") assigns user roles based on a string variable signup_code. Write an if/elif/else block: if the code is "TEACH26", role is "Instructor"; if "LEARN26", role is "Student"; else, role is "Guest".

5. A FastAPI endpoint receives an authentication token. Write an if/else block to check if auth_token is an empty string. If it is empty, assign http_status = 401. Else, assign http_status = 200.

6. You are checking the health status of a cloud-native Heroku deployment. The server_status variable can be "GREEN", "YELLOW", or "RED". Write a basic match/case block to assign an action string: "All good" for GREEN, "Check logs" for YELLOW, and "Restart Dyno" for RED.

7. For a "Desi-Earth" e-commerce checkout, apply a shipping fee. Use a ternary operator to assign shipping_fee = 0 if cart_total > 500, else assign shipping_fee = 50.

8. A hospital ward has an age restriction. Given patient_age, write an if/else block that sets admission_allowed = True only if the age is exactly 18 or older.

9. An external API returns an HTTP status code as an integer (200, 400, 404, or 500). Write a match/case block that assigns a string response_message based on these exact numbers, and use the wildcard case (_) to assign "Unknown Error" for any other number.

10. A security module tracks failed_login_attempts. Write an if/else block that sets a boolean account_locked to True if the attempts exceed 5, and False otherwise.





Intermediate Level (Focus: Nested logic, complex ternaries, and match/case guards)

11. An incoming hospital record is represented as a tuple: record = ("symptom", severity_level). For example, ("chest_pain", 8). Write a match/case block that unpacks this tuple. If the symptom is "chest_pain", assign priority 1. If "fever", assign priority 2. Otherwise, assign priority 3.

12. A ride-hailing app needs to classify vehicle types. Given vehicle_type, write a match/case block using the OR (|) pattern. If it's "bike", assign category = "2-wheeler". If it's "mini" or "prime", assign category = "car". Wildcard should assign "unknown".

13. In your ed-tech platform, determine video streaming quality. Write a nested if/else block: First check if is_premium_user is True. If so, check if bandwidth_mbps >= 10; if true, quality is "4K", else "1080p". If not a premium user, quality is "720p" regardless of bandwidth.

14. Write a nested ternary operator for a system logger. Assign log_level to "DEBUG" if environment == "dev", "INFO" if environment == "prod", and "WARN" for anything else.

15. A webhook sends deployment events as a tuple: event = ("deploy", branch_name). Write a match/case block that unpacks the tuple, but use an if guard inside the case so that it only sets trigger_build = True if the action is "deploy" AND the branch is "main".

16. E-commerce discount logic: Write an if/elif/else block that checks promo_code. If it's "NEW_USER", discount is 20%. If it's "FESTIVAL", discount is 15%. However, a user can only use "NEW_USER" if the boolean is_first_order is True. Ensure this logic is handled correctly.

17. Evaluate a valid ride request without nested ifs. Write a single if statement using logical operators (and, not) that sets ride_accepted = True only if driver_available is True, user_banned is False, and distance_km is less than 50.

18. Medical records arrive via an HL7-like stream as tuples of varying lengths: ("ADMIT", patient_id) or ("TRANSFER", patient_id, new_ward). Write a match/case block that handles both patterns and extracts the variables appropriately to print a routing message.

19. Password validation backend: Write an if/else structure that first checks if len(password) > 8. If it is, use an inner if/else to check if the string "!" or "@" is present in the password, setting is_strong = True if so.

20. A script categorizes tech blogs based on a keyword string. Write an if/elif/else block: if the keyword is exactly "solar" or "wind", category is "Renewable". If "battery", category is "Storage". Else, "General".





Advanced Level (Focus: Structural pattern matching, advanced guards, architecture)

21. You are building an API command dispatcher. The payload is a tuple: payload = ("UPDATE", "user", 1024). Write a match/case block that matches this exact 3-item structure, extracts the action, entity, and ID into variables, and handles it. Include a fallback case for malformed tuples.

22. A webhook sends live driver coordinates: location_update = (latitude, longitude, status). Write a match/case block to unpack this. Add a guard (if) to the case that triggers an "Out of Bounds Alert" if either latitude or longitude is strictly less than 0.

23. Combine a ternary operator with short-circuiting for an on-call system. Assign a final_doctor variable: it should be primary_doctor if primary_available is True, otherwise backup_doctor if backup_available is True, and if neither are available, default to the string "Emergency Ward". Write this in a single line.

24. Cloud infrastructure config parsing: You receive a nested tuple config = ("dyno", ("web", 5)). Write a match/case block that matches this nested structure, extracts the integer 5 into a variable count, and uses a guard to trigger a "Scale Warning" if count > 3.

25. Design a rudimentary rate-limiting engine. You have a tuple request = (user_tier, request_count). Write a match/case block. If tier is "free" and count < 100, allow. If tier is "pro" and count < 1000, allow. Else, block. Use structural matching with guards.

26. Course enrollment logic. Using an if/else block, first check if course_capacity > 0. If true, use a ternary operator inside the block to assign status = "Enrolled" if user_credits >= course_cost, otherwise assign "Insufficient Credits".

27. A payment gateway returns varying tuple structures: ("SUCCESS", transaction_id) or ("FAILED", error_code, retry_allowed_boolean). Write a match/case block that handles both. For the failed case, extract the boolean and use a nested if to determine if the system should re-queue the payment.

28. E-commerce inventory check. Given an integer stock_level, write a match/case block. Case 0: assign "Out of stock". Case 1, 2, or 3 (using the OR | operator): assign "Low stock alert". For any other number, use the wildcard _ with a guard (if stock_level > 10) to assign "In stock", and a final wildcard without a guard to assign "Check manually".

29. Build an Access Control List (ACL) router. You have request = (user_role, action). Write a match/case block. "admin" can do anything (match role, ignore action). "editor" can match if action is "read" | "write". "viewer" can match only if action is "read".

30. You are designing a custom routing framework from scratch. The incoming request is a string route. Write a match/case block that handles exact matches for "/home" and "/api/v1/users". Add a case that handles anything starting with "/admin" (hint: you can't use string methods like .startswith() inside the case pattern itself, so you must use a wildcard _ with an if guard) and return a 403 Forbidden.