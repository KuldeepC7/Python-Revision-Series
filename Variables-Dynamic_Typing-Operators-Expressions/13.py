# 13. A basic cryptography hashing function requires XORing a user's pin (1234) with a secret backend salt (5678). Write the expression to compute this bitwise XOR and store the ciphertext.


user_pin = 1234
secret_backend_salt = 5678

ciphertext = user_pin ^ secret_backend_salt
print(ciphertext)