# 10. Web3 and cryptographic algorithms require byte streams, not strings. Take the string `"Coder's Loop"` and convert it to a byte string using `.encode('utf-8')`. Print the result.

string = "Coder's Loop"
byte_string = string.encode('utf-8')
print(byte_string)

byte_string = string.encode('utf-16')
print(byte_string)