# 7. A FastAPI middleware checks the content type of a request. Given `content_type = "application/json"`, write an expression using a built-in string method (like `.startswith()`) to verify if it begins with `"application/"`.

content_type = 'application/json'
is_valid = content_type.startswith('application/')

if is_valid:
    print('Yes, the content type of request is starts with "application/"')
else:
    print('No, Content type of request not started with "application/"')