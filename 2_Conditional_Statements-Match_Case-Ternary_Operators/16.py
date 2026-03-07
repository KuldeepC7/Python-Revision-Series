# 16. E-commerce discount logic: Write an if/elif/else block that checks promo_code. If it's "NEW_USER", discount is 20%. If it's "FESTIVAL", discount is 15%. However, a user can only use "NEW_USER" if the boolean is_first_order is True. Ensure this logic is handled correctly.


promo_code = input('Enter your coupan code for discount: ')
discount_percentage = None

if promo_code == 'NEW_USER':
    is_first_order = bool(int(input('Press 1 for true and 0 for false: ')))
    if is_first_order:
        discount_percentage = 20
    
    else:
        discount_percentage = "You're not a new user!"

elif promo_code == 'FESTIVAL':
    discount_percentage = 15

else:
    discount_percentage = 'Wrong promo code or coupan code!'


print(discount_percentage)