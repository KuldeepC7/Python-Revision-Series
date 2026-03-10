# 14. Simulate an API rate limiter. Use a for loop to give a user exactly 3 attempts to enter a correct API key via input(). If they guess "SECRET99", break and print "Authenticated". If they fail all 3 attempts, use the for...else clause to print "Account Locked".

api = 'SECRET99'

for i in range(0, 3):
    api_key = input('Enter API key: ')
    if api_key == api:
        print('Authenticated')
        break

else:
    print('Account Locked')