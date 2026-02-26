# 3. Calculate the total fare for a ride-hailing app. The base fare is 50, the per-km rate is 12, and the distance is 8.5 km. Store the result in a total_fare variable and round it down to the nearest whole integer using only arithmetic operators (no imported math modules).

base_fare = 50
rate_per_km = 12
distance = 8.5

total_fare = base_fare + (rate_per_km * distance)

print(int(total_fare))