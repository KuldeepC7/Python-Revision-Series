# 18. You are pinging driver locations at specific intervals to save battery. Write a for loop using range() with a step argument to print the minute marks: 0, 5, 10, 15, 20, 25, 30.

import time

for i in range(0, 31, 5):
    print(i)
    time.sleep(5 * 60)