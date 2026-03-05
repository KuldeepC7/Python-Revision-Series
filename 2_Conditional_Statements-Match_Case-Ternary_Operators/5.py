# 5. A FastAPI endpoint receives an authentication token. Write an if/else block to check if auth_token is an empty string. If it is empty, assign http_status = 401. Else, assign http_status = 200.

auth_token = 'fsh4r29i0wr90hjsfbf84wurjfsbefb'
http_status = 200 if auth_token != '' else 401
print(http_status)