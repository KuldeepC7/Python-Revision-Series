# 4. An ed-tech platform ("Coder's Loop") assigns user roles based on a string variable signup_code. Write an if/elif/else block: if the code is "TEACH26", role is "Instructor"; if "LEARN26", role is "Student"; else, role is "Guest".

signup_code = ''

user_role = 'Student' if signup_code=='LEARN26' else ('Instructor' if signup_code=='TEACH26' else 'Guest')

print(user_role)