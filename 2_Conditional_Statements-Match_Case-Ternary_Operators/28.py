# 28. E-commerce inventory check. Given an integer stock_level, write a match/case block. Case 0: assign "Out of stock". Case 1, 2, or 3 (using the OR | operator): assign "Low stock alert". For any other number, use the wildcard _ with a guard (if stock_level > 10) to assign "In stock", and a final wildcard without a guard to assign "Check manually".

stock_level = int(input('What is stock level current: '))
current_stock = None

match stock_level:
    case 0:
        current_stock = 'Out of stock'
    
    case 1 | 2 | 3:
        current_stock = 'Low stock alert'
    
    case _:
        if stock_level > 10:
            current_stock = 'In stock'
        
        else:
            current_stock = 'Check manually'

print(current_stock)