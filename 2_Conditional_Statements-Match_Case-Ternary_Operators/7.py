# 7. For a "Desi-Earth" e-commerce checkout, apply a shipping fee. Use a ternary operator to assign shipping_fee = 0 if cart_total > 500, else assign shipping_fee = 50.

cart_total = float(input("Enter cart total: "))

shipping_fee = 0 if cart_total > 500 else 50
print(shipping_fee)