# 25. Given the cache_key integer from the previous question, write the expressions using the bitwise right shift and bitwise AND (with a hexadecimal mask) to unpack and retrieve the original endpoint ID and user ID.

# endpoint_ID = 15
# user_ID = 1024

# cache_key = (endpoint_ID << 16) | user_ID
# print(cache_key)


cache_key = 984064

endpoint_ID = cache_key >> 16





# Unpacking the Cache Key
# You successfully packed the key in Q24: cache_key = (endpoint_ID << 16) | user_ID.
# To reverse it:

# endpoint_ID: We shifted it left by 16 to pack it. So we shift it right by 16 to unpack it.
# endpoint = cache_key >> 16

# user_ID: It occupies the lower 16 bits. We extract it using a mask of sixteen 1s (which is 0xFFFF or 65535 in decimal), just like we did in Q22.
# user = cache_key & 0xFFFF