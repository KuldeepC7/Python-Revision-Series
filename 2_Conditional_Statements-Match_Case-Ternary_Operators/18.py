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