# 27. In a ride-hailing app's surge pricing algorithm, demand_multiplier is calculated as active_users / available_drivers. Write an expression that safely computes this, but assigns 1.0 if available_drivers is 0, using strictly logical short-circuiting (and / or) to prevent a ZeroDivisionError.

active_users = 5
available_drivers = 1
demand_multiplier = (available_drivers == 0) * 1.0 + (available_drivers > 0) * active_users/available_drivers

print(demand_multiplier)