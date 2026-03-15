# 13. Format a doctor's availability schedule. Using the older `.format()` method (which is still heavily used in legacy codebases), inject "Dr. Sharma" and "10:00 AM" into this template: `"{} is available at {}"`.

doctors_availability_schedule = "{} is available at {}".format('Dr. Sharma', '10:00 AM')
print(doctors_availability_schedule)