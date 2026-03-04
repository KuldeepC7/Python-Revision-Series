# 18. In Web3, smart contract states often use bitwise inversion. Given an 8-bit permission mask mask = 0b10101010, apply the bitwise NOT operator (~) and explain in a comment why the result appears as a negative integer in Python.

mask = 0b10101010
inversion_mask = ~mask
print(inversion_mask)

#Computers store integers using "Two's Complement". The very first bit on the far left is the "sign bit" (0 for positive, 1 for negative). When you use ~ to flip all the bits, you are also flipping the sign bit, turning a positive number into a negative one. 

# Mathematically, ~x is always equal to -(x + 1).