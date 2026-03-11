# 30. Two-Pointer Simulation: You have a tuple of sorted integers (1, 2, 3, 4, 5, 6). Use a while loop with two manual index variables: left_index = 0 and right_index = 5. In each iteration, print the values at both indexes, increment left_index by 1, and decrement right_index by 1. Stop the loop when left_index is greater than or equal to right_index.

sorted_integers = (1, 2, 3, 4, 5, 6)

left_index = 0
right_index = 5

while left_index <= right_index:
    print(f'values: {left_index} and {right_index}')
    
    left_index += 1
    right_index -= 1