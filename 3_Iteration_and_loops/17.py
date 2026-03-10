# 17. You are writing a parser for a Hospital Management System that reads HL7-like messages from a tuple: ("ADMIT", "", "TRANSFER", "DISCHARGE"). Use a for loop to process them. If the string is empty "", use continue to skip it.

message = ('ADMIT', '', 'TRANSFER', 'DISCHARGE')

for status in message:
    if status:
        print(status)
    else:
        continue