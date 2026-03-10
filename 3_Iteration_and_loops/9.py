# 9. Calculate total daily revenue for your Hooka and Ghosa site. Create a variable total = 0. Write a for loop that runs 3 times. Inside, use input() to ask for the revenue of an order, convert it to an integer, and add it to the total. Print the final total.

total = 0
for i in range(3):
    revenue_of_order = int(input('What is revenue of current order: '))
    total += revenue_of_order

print(total)