# 23. To optimize a data-processing script for an AI tool, swap the values of two variables, feature_x and feature_y, without using a temporary third variable. Do this first using Python's tuple unpacking, and then write a separate solution using only bitwise XOR operations.

feature_x = 5
feature_y = 7

# data = (feature_x, feature_y)
# feature_y, feature_x = data

# print(feature_x)
# print(feature_y)

feature_x = feature_x | feature_y
feature_y = feature_x ^ feature_y
feature_x = feature_x ^ feature_y

print(feature_x)
print(feature_y)