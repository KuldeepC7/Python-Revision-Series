# 23. Finding the Minimum: You receive a tuple of nearby cab distances: (12, 8, 15, 3, 9). Without using the built-in min() function, write a for loop that iterates through the tuple and continually updates a shortest_distance variable to find the smallest number.

nearby_cab_distances = (12, 8, 15, 3, 9)

shortest_distance = 0

for distance in nearby_cab_distances:
    if nearby_cab_distances[0] == distance:
        shortest_distance = distance
    
    else:
        if shortest_distance > distance:
            shortest_distance = distance

print(shortest_distance)