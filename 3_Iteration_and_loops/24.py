# 24. Batch Processing: Your backend needs to process 100 data rows using range(1, 101). However, to prevent memory overflow, you must trigger a garbage collection cycle every 20 rows. Write a for loop that iterates through the 100 rows, and uses the modulo operator (%) to print "Clearing memory..." exactly on rows 20, 40, 60, 80, and 100.

for row in range(1, 101):
    # print(row)
    # if row % 20 == 0:
    #     print("Clearing memory.....")
    if row % 20 != 0:
        print(row)
    
    else:
        print("Clearing memory.....")