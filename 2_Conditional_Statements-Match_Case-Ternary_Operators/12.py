# 12. A ride-hailing app needs to classify vehicle types. Given vehicle_type, write a match/case block using the OR (|) pattern. If it's "bike", assign category = "2-wheeler". If it's "mini" or "prime", assign category = "car". Wildcard should assign "unknown".

vehicle_type = input('Vehicle Type: ')
category = ''

match vehicle_type:
    case 'bike':
        category = '2-wheeler'
    
    case 'mini' | 'prime':
        category = 'car'
    
    case _:
        category = 'unknown'

print(category)