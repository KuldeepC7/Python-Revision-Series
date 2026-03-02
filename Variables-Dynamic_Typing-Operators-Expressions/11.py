# 11. An e-commerce cart calculation applies a discount. Write an expression using short-circuit logical operators (and / or) that assigns the value 0.10 to a variable discount_rate if coupon_applied is True, and assigns 0.0 if it is False. (Do not use if-else).


coupan_applied = True

# discount_rate = (coupan_applied > 0) * 0.10 or (coupan_applied <= 0) * 0.0

discount_rate = coupan_applied and 0.10 or 0.0

print(discount_rate)