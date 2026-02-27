# 19. Calculate the division of a server's uptime (e.g., uptime_hours = 45) by 24 to get the days and remaining hours. Store the quotient and the remainder in two separate variables using the floor division (//) and modulo (%) operators.


uptime_hours = 45

remaining_days = uptime_hours / 24

remaining_hours = uptime_hours % 24

print("Remaining days for server uptime", remaining_days)
print("Remaining hours for server uptime", remaining_hours)