# 29. Build an Access Control List (ACL) router. You have request = (user_role, action). Write a match/case block. "admin" can do anything (match role, ignore action). "editor" can match if action is "read" | "write". "viewer" can match only if action is "read".

request_str = input('Access control request: ')
request = tuple(request_str.split(','))
user_role, action = request

match user_role:
    case 'admin':
        print('can do anything')
    
    case 'editor':
        if action == 'read' or action == 'write':
            print('access granted')
        else:
            print('Not allowed')

    case 'viewer':
        if  action == 'read':
            print('Only reading allowed')
        else: 
            print('request for wrong permission')