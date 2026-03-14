# 11. You are parsing a verified JWT authentication token header that comes back from a secure microservice as bytes: `b'{"alg":"HS256"}'`. Use `.decode('utf-8')` to convert it back to a standard Python string.

token_header = b'{"alg":"HS256"}'

token_header_decoded = token_header.decode('utf-8')
print(token_header_decoded)