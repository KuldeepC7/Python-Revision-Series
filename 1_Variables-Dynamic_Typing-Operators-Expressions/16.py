# 16. A background task calculates the size of a file upload. Given file_size_bytes = 1048576, use the bitwise right shift operator to convert this value directly into Megabytes (shifting by 20 bits).


file_size_bytes = 1048576
file_size_megabytes = file_size_bytes >> 20
print(file_size_megabytes)