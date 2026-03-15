# 14. A raw HTTP GET request line arrives via a TCP socket: `"GET /api/v1/rides HTTP/1.1"`. Use `.split()` to extract and print *only* the routing path (`"/api/v1/rides"`).

raw_http_request = "GET /api/V1/rides HTTP/1.1"
routing_path = (raw_http_request.split(' '))[1]
print(routing_path)