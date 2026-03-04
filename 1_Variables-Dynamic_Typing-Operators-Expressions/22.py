# 22. You are building a decentralized Web3 application where transaction signatures are heavily compressed. Extract the lower 4 bits of an integer payload = 205 (binary 11001101) using a bitwise mask and the AND operator.


# You have payload = 205 (11001101). You only want the last 4 bits (1101). You use an AND (&) mask. If you AND something with 1, it keeps its value. If you AND it with 0, it becomes 0.
# We want to mask it with 00001111 (which is 15 in decimal).


payload = 205
lower_4_bits = payload & 15  # Result is 13 (binary 1101)

print(lower_4_bits)