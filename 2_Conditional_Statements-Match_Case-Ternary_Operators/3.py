# 3. Rewrite the logic from Question 2 using a single Python Ternary operator to assign the boolean value to booking_confirmed in one line.

# value_if_true if condition else value_if_false

wallet_balance = 52
estimated_fare = 55
booking_confirmed = True if estimated_fare < wallet_balance else False

print(booking_confirmed)