# 26. Course enrollment logic. Using an if/else block, first check if course_capacity > 0. If true, use a ternary operator inside the block to assign status = "Enrolled" if user_credits >= course_cost, otherwise assign "Insufficient Credits".

course_capacity = 2
user_credits = 1000
course_cost = 250
status = None

if course_capacity > 0:
    status = 'Enrolled' if user_credits >= course_cost else 'Insufficient Credits'

else: 
    status = 'Nothing'


print(status)