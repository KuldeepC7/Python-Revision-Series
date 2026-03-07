# 25. Design a rudimentary rate-limiting engine. You have a tuple request = (user_tier, request_count). Write a match/case block. If tier is "free" and count < 100, allow. If tier is "pro" and count < 1000, allow. Else, block. Use structural matching with guards.

request = ('free', 75)
allow_or_not = None

user_tier, request_count = request

match user_tier:
    case 'free':
        if request_count < 100:
            allow_or_not = 'allow'
        else:
            allow_or_not = 'block'
    
    case 'pro':
        if request_count < 1000:
            allow_or_not = 'allow'
        else:
            allow_or_not = 'block'
    
    case _:
        allow_or_not = 'block'

print(allow_or_not)