# 30. You are designing a custom routing framework from scratch. The incoming request is a string route. Write a match/case block that handles exact matches for "/home" and "/api/v1/users". Add a case that handles anything starting with "/admin" (hint: you can't use string methods like .startswith() inside the case pattern itself, so you must use a wildcard _ with an if guard) and return a 403 Forbidden.


request = input('Route: ')

match request:
    case '/home':
        print('Redirecting to home')
    
    case '/api/v1/users':
        print('Redirecting to users page')
    
    case _:
        if request.startswith('/admin'):
            print('403 Forbidden')
        
        else:
            print('Wrong route')