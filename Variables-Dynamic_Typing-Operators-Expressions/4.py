# 4. You are generating AI content and have a boolean variable is_premium_user and an integer daily_generation_limit = 10. Write a single mathematical expression that doubles the limit only if is_premium is True, leveraging the fact that booleans evaluate to integers in Python.

is_premium_user = True
daily_generation_limit = 0



daily_generation_limit = (is_premium_user > 0) * 20 + (is_premium_user <= 0) * 10 #How this line is working, explain me

print(daily_generation_limit)