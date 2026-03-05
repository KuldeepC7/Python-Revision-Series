# 2. In a ride-hailing app, a user is trying to book a cab. Write a simple if/else statement that checks if wallet_balance is greater than or equal to estimated_fare. If it is, assign booking_confirmed = True, otherwise assign False.

wallet_balance = 70
estimated_fare = 50

if estimated_fare < wallet_balance:
    booking_confirmed = True
    print(booking_confirmed)

else:
    booking_confirmed = False
    print(booking_confirmed)
