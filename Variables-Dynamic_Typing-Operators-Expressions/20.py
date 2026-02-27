# 20. You have a string variable user_input. Ensure that a final_username variable defaults to "Guest" if user_input is empty, utilizing the or operator's truthiness short-circuit behavior.


user_input = 'Kuldeep'

# Explain me how this is happening
user_input = (user_input != '') * user_input or (user_input == '') * 'Guest'

print(user_input)