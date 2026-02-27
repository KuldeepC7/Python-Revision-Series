# 30. You are chaining multiple validation checks for a login endpoint: is_valid_email(), is_rate_limited(), and check_password(). Construct a single, unbroken logical expression where check_password() is never executed if the email is invalid or if the user is rate-limited, relying entirely on Python's left-to-right short-circuit sequence.


def is_valid_email():
    return True    

def is_rate_limited():
    return True

def check_password():
    return True

l_to_r = (check_password() and (is_valid_email() and is_rate_limited))

print(l_to_r) 