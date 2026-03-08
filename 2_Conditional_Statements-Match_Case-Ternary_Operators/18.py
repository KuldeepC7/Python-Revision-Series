# 18. Medical records arrive via an HL7-like stream as tuples of varying lengths: ("ADMIT", patient_id) or ("TRANSFER", patient_id, new_ward). Write a match/case block that handles both patterns and extracts the variables appropriately to print a routing message.

record = ('TRANSFER', 1257, "OT")
routing_message = None

match (record[0]):
    case 'ADMIT':
        routing_message = f'Patient with id {record[1]}, needs to be admit'
    
    case 'TRANSFER':
        if len(record) > 2:
            routing_message = f'Pateint with id {record[1]}, needs to be transfer in {record[2]}'
        else:
            routing_message = "NO ward name"

print(routing_message)






# new solution: 

# record = ('TRANSFER', 1257, "OT")

# match record:
#     # Matches a 2-item tuple starting with "ADMIT"
#     # Automatically creates a 'patient_id' variable!
#     case ("ADMIT", patient_id):
#         print(f'Patient {patient_id} needs to be admitted')
    
#     # Matches a 3-item tuple starting with "TRANSFER"
#     # Automatically extracts 'patient_id' and 'new_ward'!
#     case ("TRANSFER", patient_id, new_ward):
#         print(f'Patient {patient_id} transfers to {new_ward}')
        
#     case _:
#         print("Unknown record format")