# 21. You are building an API command dispatcher. The payload is a tuple: payload = ("UPDATE", "user", 1024). Write a match/case block that matches this exact 3-item structure, extracts the action, entity, and ID into variables, and handles it. Include a fallback case for malformed tuples.


payload = ('UPDATE', 'user', 1024)

# match len(payload):
#     case 3:
#         if isinstance(payload[0], str) and isinstance(payload[1], str) and isinstance(payload[2], int):
#             action,entity,ID = payload
#             print(action, entity, ID)
#             print(type(action), type(entity), type(ID))
        
#         else: 
#             print('malformed tuple')
    
#     case _:
#         print('malformed tuple')


match payload:
    case (action, entity, ID):
        if isinstance(action, str) and isinstance(entity, str) and isinstance(ID, int):
            print(action, entity, ID)
            print(type(action), type(entity), type(ID))
        else:
            print('Malformed tuple')
    
    case _:
        print('Malformed tuple')