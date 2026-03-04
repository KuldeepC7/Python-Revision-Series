# 21. In Python, small integers are cached by the interpreter. Assign a = 256 and b = 256, then x = 257 and y = 257. Write the expressions to compare a is b, and x is y. In a comment, explain why the identity operator yields different results and what this means for backend memory optimization.


a = 256
b = 256
x = 257
y = 257

print(a is b)
print(x is y)

'''
The python interpreter holds a variable's value in memory with a particular address. And it doesn't create a new memory address to store the same value, like if we created a variable a with value 256, then it holds this 256 value with a particular memory address. And when create another variable lets say b with the same value 256, then the interpreter will points b variable to also the same memory address of a variable. And when identity operator checks whether they are in same memory address and have similar values or not, it found that they both have same value and points to the same memory address.

This is beneficial in memory optimization of backend because, for different variable objects with same value, all variables points to the same memory address and it will use less memory. There will be less memory consumption.  
'''