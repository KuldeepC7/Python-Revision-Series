### Basic Level (Focus: Core Methods, Slicing, and Formatting)

1. You are building the notification engine for the Safar ride-hailing app. Create variables for `driver_name` and `vehicle_number`. Write an `f-string` to generate a welcome message: "Your driver, [Name], is arriving in [Number]".

2. A patient's blood pressure data from legacy medical hardware at Kataria Multispecialist Hospital arrives with messy whitespace: `"  120/80 \n"`. Use the `.strip()` method to clean it and store it in a new variable.

3. In your Coder's Loop platform, a course video is uploaded with the filename `"intro_to_python_programming"`. Use the `.replace()` method to change all underscores to spaces for the frontend display.

4. A customer searches for a product on your Hooka and Ghosa site: `"   Dung Cakes   "`. Chain the `.strip()` and `.lower()` methods together in a single line to normalize this search query to `"dung cakes"`.

5. Prove the concept of string immutability. Assign `status = "Active"`. Try to change the first letter to "I" using indexing (e.g., `status[0] = "I"`). In a comment, explain why Python throws a `TypeError`.

6. You have a comma-separated string of TCS Ignite exam centers: `"Indore,Bhopal,Gwalior"`. Use `.split(",")` to break this string apart, and write a `for` loop to print each city on a new line.

7. A FastAPI middleware checks the content type of a request. Given `content_type = "application/json"`, write an expression using a built-in string method (like `.startswith()`) to verify if it begins with `"application/"`.

8. You have a tuple of command arguments in Manjaro Linux: `("sudo", "systemctl", "restart", "nginx")`. Use the `.join()` method with a space separator `" "` to combine them into a single executable string command.

9. A server path is formatted as `"/var/log/nginx/error.log"`. Use `.split("/")` and negative indexing (e.g., `[-1]`) on the resulting sequence to extract just the file name (`"error.log"`).

10. Web3 and cryptographic algorithms require byte streams, not strings. Take the string `"Coder's Loop"` and convert it to a byte string using `.encode('utf-8')`. Print the result.





### Intermediate Level (Focus: Parsing, Chaining, Raw Strings, and Decoding)

11. You are parsing a verified JWT authentication token header that comes back from a secure microservice as bytes: `b'{"alg":"HS256"}'`. Use `.decode('utf-8')` to convert it back to a standard Python string.

12. A background script processes local files on a Windows machine. The path is `"C:\new_folder\test.txt"`. Explain in a comment why this string will break your code, and rewrite the variable assignment using a raw string (`r"..."`).

13. Format a doctor's availability schedule. Using the older `.format()` method (which is still heavily used in legacy codebases), inject "Dr. Sharma" and "10:00 AM" into this template: `"{} is available at {}"`.

14. A raw HTTP GET request line arrives via a TCP socket: `"GET /api/v1/rides HTTP/1.1"`. Use `.split()` to extract and print *only* the routing path (`"/api/v1/rides"`).

15. An SMS gateway integration strictly requires messages to be under 160 characters. Given `sms_body = "Your ride is confirmed..."`, write an `if/else` block using an f-string to print "Sent" if valid, or "Failed: Length is {length}" if it exceeds the limit.

16. You are generating unique SKUs for e-commerce products. You have `category = "HOOKA"` and `product_id = 45`. Generate a string formatted exactly as `"HOOKA-00045"` using f-string padding/formatting (forcing the integer to be 5 digits with leading zeros).

17. In blockchain interactions, hexadecimal strings are standard. Take a string `wallet_address = "0x1A2B"`, encode it to `ascii` bytes, and write a condition to check if the *byte string* starts with `b"0x"`.

18. A driver registers their phone number as `"+91-98765-43210"`. Chain `.replace()` methods to remove both the `+91-` country code prefix and the internal dash, resulting in a clean 10-digit string.

19. Extract the domain from a student's email address on your ed-tech platform. Given `email = "student@gmail.com"`, use `.split("@")` and retrieve the second part (the domain) using an index.

20. Parse a CSV row manually: `line = "Kuldeep,22,Python"`. Use `.split(",")` to unpack the string directly into three variables: `name`, `age`, and `skill`. Print them in an f-string.





### Advanced Level (Focus: Memory Efficiency, Data Cleaning, and Complex Formatting)

21. Write a URL slug generator for blog posts. Take the string `title = "  TCS Ignite 2026: Preparation Guide!  "`. In one chained execution: strip whitespace, convert to lowercase, replace spaces with hyphens, and remove colons and exclamation marks.

22. You are logging a critical server error. Create a multiline string using triple quotes (`"""`) that acts as an f-string. Inject variables for `timestamp`, `error_code`, and `user_id`, ensuring the text alignment looks clean when printed to the console.

23. Simulate AES encryption preparation. Take the string `secret = "my_password"`. Encode it to `utf-8` bytes. Then, write a `for` loop that iterates over the byte string. Print the raw integer value of each byte (Python does this natively when iterating over bytes).

24. A malformed webhook query string arrives from a payment gateway: `"?driver=kuldeep&&&status=active&&"`. Chain `.strip("&")` and `.replace("&&&", "&")` to clean it into a valid query string: `"?driver=kuldeep&status=active"`.

25. Backend memory efficiency: Explain in a detailed comment why creating an empty string `result = ""` and continually adding to it in a loop (`result += new_char`) is highly inefficient in Python due to string immutability, and state the preferred alternative.

26. A user inputs an exam date as `"2026-02-21"`. Use `.split("-")` to unpack this into `year`, `month`, and `day` variables in a single line. Then, reformat and print it as `"DD/MM/YYYY"` using an f-string.

27. Parse a legacy fixed-width text record: `record = "PATIENT12345CRITICAL"`. The first 7 characters are the prefix, the next 5 are the ID, and the rest is the status. Use string slicing (`[start:stop]`) to extract these into three distinct variables.

28. Handle strict Unicode decoding. Encode the string `"🚀 To the moon!"` into `utf-8` bytes. Then, try to decode that byte string using the `.decode('ascii', errors='ignore')` method. Print the result and observe how the system drops the emoji to prevent a crash.

29. You have a very long SQL query. Use implicit string concatenation (placing strings next to each other inside parentheses without the `+` operator) to format a multiline `SELECT` query cleanly in your code without using triple quotes.

30. An API responds with a secure header: `header = "Authorization: Bearer abcdef12345"`. Write an `if` block that checks if the string `.startswith("Authorization: Bearer ")`. If it does, use string slicing to extract just the token (`"abcdef12345"`) by slicing off the exact length of the prefix. Avoid using `.split()`.