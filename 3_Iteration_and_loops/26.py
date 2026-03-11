# 26. State Machine: Simulate the lifecycle of a ride request. Create a variable state = "SEARCHING". Write a while True loop. Inside, use a match/case block based on state.
#     If SEARCHING, wait for input("Found driver? (y/n): "), if 'y', change state to "ARRIVED".
#     If ARRIVED, wait for input("Start trip? (y/n): "), change to "IN_TRANSIT".
#     If IN_TRANSIT, wait for input("End trip? (y/n): "), change to "COMPLETED".
#     If COMPLETED, break the loop.

state = 'SEARCHING'

while True:
    match state:
        case 'SEARCHING':
            driver_found = input('Found driver? (y/n): ')
            if driver_found == 'y':
                state = 'ARRIVED'
        
        case 'ARRIVED':
            trip_start = input('Start trip? (y/n): ')
            if trip_start == 'y':
                state = 'IN_TRANSIT'
            
        case 'IN_TRANSIT':
            trip_end = input('End trip? (y/n): ')
            if trip_end == 'y':
                state = 'COMPLETED'
        
        case 'COMPLETED':
            print('Trip Completed :)')
            break