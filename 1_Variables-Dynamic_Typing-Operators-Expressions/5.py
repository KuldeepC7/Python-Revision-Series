# 5. Given two variables representing user IDs retrieved from a Supabase database, user_id_1 = "uuid-1234" and user_id_2 = "uuid-1234", write one expression to check if their values are equal, and another expression to check if they are the exact same object in memory.

user_id_1 = 'uuid-1234'
user_id_2 = 'uuid-1234'

print(user_id_1 == user_id_2)
print(id(user_id_1) == id(user_id_2))
print(id(user_id_1))
print(id(user_id_2))