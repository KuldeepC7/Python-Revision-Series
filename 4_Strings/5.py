# 5. Prove the concept of string immutability. Assign `status = "Active"`. Try to change the first letter to "I" using indexing (e.g., `status[0] = "I"`). In a comment, explain why Python throws a `TypeError`.

status = 'Active'

status[0] = 'I'
print(status)
# Strings are immutable, means we cant update them directly based on their indexes and cant assign new items on specific indexes. 
# give me a more detailed explanation of why strings are immutable
