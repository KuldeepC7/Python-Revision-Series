# 9. A server path is formatted as `"/var/log/nginx/error.log"`. Use `.split("/")` and negative indexing (e.g., `[-1]`) on the resulting sequence to extract just the file name (`"error.log"`).

server_path = '/var/log/nginx/error.log'
file_name = server_path.split('/')
print(file_name[-1])