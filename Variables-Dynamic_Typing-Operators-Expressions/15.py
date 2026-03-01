# 15. Following the previous question, write an expression using the bitwise AND operator to verify if a given user_preferences integer contains the FLAG_NO_PROMO bit.

FLAG_ANONYMOUS = 1
FLAG_NO_PROMO = 2

user_preferences = FLAG_ANONYMOUS | FLAG_NO_PROMO
print(FLAG_ANONYMOUS == user_preferences & FLAG_ANONYMOUS)