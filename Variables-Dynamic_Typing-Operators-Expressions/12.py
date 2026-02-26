# 12. You are managing authentication lists. token_a = [1, 2, 3] and token_b = [1, 2, 3]. Write code demonstrating why token_a == token_b evaluates to True, but token_a is token_b evaluates to False.


#Explain me this program, why the results are different
token_a = [1,2,3]
token_b = [1,2,3]

a = 5
b = 5

print(token_a == token_b) # checks whether the value is same or not of both the lists

print(token_a is token_b) # Checks whether are they holds same memory address or not, compare their memory address. And list is mutable and stores ts elements in adjacent memory addresses, but two lists with the same value and elements are stored in different memory address.

print(id(token_a) == id(token_b)) 
