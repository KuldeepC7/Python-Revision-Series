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







'''
Guards vs. Nested Ifs (Questions 15, 22, 24, 28, 30)
When asked to use an "if guard," you placed an if statement inside the case block.

How to analyze this: A "guard" is a special feature of match/case. It is an if statement attached directly to the case line. If the pattern matches, but the guard is False, Python skips it and keeps looking for other cases.

The Backend Fix (Looking at Q30: The Custom Router):

Python
request = '/admin/settings'

match request:
    case '/home':
        print('Redirecting to home')
    
    # THIS is a guard. It sits on the same line as the case.
    case _ if request.startswith('/admin'):
        print('403 Forbidden')
        
    case _:
        print('Wrong route')
'''