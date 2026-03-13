# 1. You are building the notification engine for the Safar ride-hailing app. Create variables for `driver_name` and `vehicle_number`. Write an `f-string` to generate a welcome message: "Your driver, [Name], is arriving in [Number]".


driver_name = input('Enter driver name: ')
vehicle_number = input('Enter vehicle number: ')

print(f'Your driver, {driver_name}, is arriving in {vehicle_number}')