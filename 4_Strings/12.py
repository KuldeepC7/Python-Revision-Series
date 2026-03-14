# 12. A background script processes local files on a Windows machine. The path is `"C:\new_folder\test.txt"`. Explain in a comment why this string will break your code, and rewrite the variable assignment using a raw string (`r"..."`).

path = 'C:\new_folder\test.txt'

#This string will break the code because we are using escape sequencers or characters in the string like '\n' and '\t'. So when we print it, the '\n' will print the upcoming characters after the 'C:' on a new line and similarly the '\t' will give a tab space.

print(path)

path2 = r"C:\new_folder\test.txt"
print(path2)