# 15. Grid search for a map feature. Write a nested for loop where x ranges from 0 to 2 and y ranges from 0 to 2. If the coordinate is exactly x=1 and y=1 (representing a blocked road), use continue to skip printing that specific coordinate.

for x in range(3):
    for y in range(3):
        if x == 1 and y == 1:
            continue
        else:
            print(x, y)