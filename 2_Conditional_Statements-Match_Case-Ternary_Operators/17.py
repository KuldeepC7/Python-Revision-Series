# 17. Evaluate a valid ride request without nested ifs. Write a single if statement using logical operators (and, not) that sets ride_accepted = True only if driver_available is True, user_banned is False, and distance_km is less than 50.

user_banned = bool(int(input('Is user banned or not: ')))
driver_available = bool(int(input('Is driver available: ')))
distance_in_km = eval(input('Enter distance in km: '))

ride_accepted = True if (driver_available and not user_banned and (distance_in_km < 50)) else False

# ride_accepted = False
# if not user_banned:
#     driver_available = bool(int(input('Is driver available: ')))
#     if driver_available:
#         distance_in_km = eval(input('Enter distance in km: '))
#         if distance_in_km < 50:
#             ride_accepted = True

print(ride_accepted)