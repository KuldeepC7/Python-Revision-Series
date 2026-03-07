# 22. A webhook sends live driver coordinates: location_update = (latitude, longitude, status). Write a match/case block to unpack this. Add a guard (if) to the case that triggers an "Out of Bounds Alert" if either latitude or longitude is strictly less than 0.


location_update_str = input('Enter cordinates and status with separation of commas and also between x & y cordinates: ')
location_update_tuple = tuple(location_update_str.split(','))

if len(location_update_tuple) == 3:
    location_update = (int(location_update_tuple[0]), int(location_update_tuple[1]), location_update_tuple[2])
    match location_update:
        case (latitude, longitude, status):
            if (latitude > 0 and longitude > 0):
                print(True, location_update)
            else:
                print(False, "Out of Bounds Alert")
    
        case _:
            print(False, 'Out of Bounds Alert')

else:
    print("Tuple is malformed!")