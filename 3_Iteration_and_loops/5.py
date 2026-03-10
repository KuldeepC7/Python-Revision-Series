# 5. A backend service processes a tuple of HTTP status codes: (200, 201, 404, 500, 200). Write a for loop to iterate through them. If the code is 404 or 500, use the continue statement to skip processing it and move to the next code.

http_status_codes = (200, 201, 404, 500, 200)

for status_code in http_status_codes:
    if status_code == 404 or status_code == 500:
        continue
    else:
        print(f"{status_code}: Success")