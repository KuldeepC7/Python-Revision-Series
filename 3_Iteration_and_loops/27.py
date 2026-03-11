# 27. String Parsing without Split: You receive a raw string of comma-separated patient IDs from a legacy system: "101,102,103,". Write a for loop to iterate through every character. Append characters to a temporary current_id string. When you encounter a comma ",", print the current_id, reset it to empty, and continue.

patient_ids = '101,102,103,'
current_id = ''

for character in patient_ids:
    if character == ',':
        print(current_id)
        current_id = ''
    else:
        current_id += character