# 14. A hospital management system tracks patient privacy preferences using flags: FLAG_ANONYMOUS = 1 (0001) and FLAG_NO_PROMO = 2 (0010). Use a bitwise operator to create a user_preferences integer that holds both flags simultaneously.

FLAG_ANONYMOUS = 1
FLAG_NO_PROMO = 2

user_preferences = FLAG_ANONYMOUS | FLAG_NO_PROMO
print(user_preferences)
print(FLAG_ANONYMOUS == user_preferences & FLAG_ANONYMOUS)