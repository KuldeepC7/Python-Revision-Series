# 9. In a ride-hailing backend, a driver is considered dispatchable if is_online is True and on_trip is False. Write the logical expression to represent this dispatchable status.

is_online = True
on_trip = False

is_dispatchable = is_online and not on_trip
print("Driver is dispatchable: ", is_dispatchable)