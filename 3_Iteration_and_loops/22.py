# 22. Data Pagination Simulation: You have 15 product IDs in an e-commerce database. Instead of a list, just use range(1, 16). Write an outer while True loop that asks the user input("Press Enter for next page, or type 'quit': "). Inside, use an inner for loop to print exactly 5 items per page. (Hint: you will need to track the current index variable manually).


# items = ['something', 'one', 'two', 'three', 'four']

index_variable = 3
pagination_variable = 1

while True:
    if index_variable == 0:
        break

    else: 
        command = input('Press enter for next page, or type "quit": ')
        if command == 'quit':
            break

        elif command == '':
            for i in range (pagination_variable, pagination_variable + 5):
                print(f'Product {i} with product id: {i}')
            
            pagination_variable += 5
            index_variable -= 1
        
        else:
            print('Enter correct command!')