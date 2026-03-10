# 2. In a ride-hailing app, a countdown timer is displayed to the user while waiting for a cab. Write a while loop that starts at 5, prints the current minute, and decrements by 1 until it reaches 0.

import time

minutes = 5
while minutes != 0:
    print(minutes)
    time.sleep(60)
    minutes -= 1