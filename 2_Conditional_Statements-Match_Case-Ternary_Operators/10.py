# 10. A security module tracks failed_login_attempts. Write an if/else block that sets a boolean account_locked to True if the attempts exceed 5, and False otherwise.

failed_login_attempts = int(input('No. of login attempts: '))

# account_locked = True if failed_login_attempts > 5 else False

account_locked = failed_login_attempts > 5

print(account_locked)