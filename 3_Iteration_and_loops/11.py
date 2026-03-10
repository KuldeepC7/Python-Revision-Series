# 11. A driver in your ride-hailing app has a daily earnings goal of 500 Rs. Write a while loop that continues to ask for a ride_fare via input() and adds it to their total earnings. The loop should stop automatically as soon as the total earnings are greater than or equal to 500.

daily_earning_goal = 500
riders_earning_today = 0

while daily_earning_goal >= riders_earning_today:
    ride_fare = float(input('Enter current ride fare: '))
    riders_earning_today += ride_fare

print(riders_earning_today)