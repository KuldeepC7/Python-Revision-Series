# 28. Create a variable secret_key pointing to a list [1, 2, 3]. Assign backup_key = secret_key. Modify the first element of backup_key. Evaluate the identity (is) and equality (==) of the two variables. In a comment, explain the security implications of variable mutability when handling data references in a backend system.



secret_key = [1, 2, 3]
backup_key = secret_key
backup_key[0] = 5

print(secret_key)
print(backup_key)

print(secret_key == backup_key)
print(backup_key is secret_key)

'''
The security implications of variable mutability when handling data references in a backend system:
- So here data references means that the secret_key and its value is a refernce for the backup_key. And the backup key is referencing to the same memory address and value that of the secret_key.

- So when we change/update/add/delete any element of any one of the data objects/lists, then it will change that value in memory address (which is shared by both) directly. Hence the other data object/list will be also get affected.

- In this case we are changing the first element of backup_key, and both (secret_key and backup_key) has the same memory address, so it will change the first element in that shared memory address. And the first element of secret_key will also get change in this case.

- Now in real backend system, it will cause issue by breaking the working functionality of secret_key, when it get modified. So we never have to make any backup of anything in backend by direct referencing it to the main working variable or any data object. And if we modify the data in backup object, it will also change in the main working data object.

'''