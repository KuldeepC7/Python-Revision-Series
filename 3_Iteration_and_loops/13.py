# 13. E-commerce product variations: You have a tuple of Hooka sizes ("Small", "Large") and a tuple of flavors ("Mint", "Apple"). Write a nested for loop (one inside the other) to print all possible product combinations (e.g., "Small Mint").

hooka_size = ('Small', 'Large')
flavors = ('Mint', 'Apple')

for size in hooka_size:
    for flavor in flavors:
        print(size, flavor)