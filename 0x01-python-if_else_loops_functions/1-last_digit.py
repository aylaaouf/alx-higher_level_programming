#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = str(number)[-1]
last_int = int(last)
if last_int > 5 and number > 0:
    print(f"Last digit of {number} is {last} and is greater than 5")
elif last_int < 6 and last_int != 0 and number > 0 :
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
elif number < 0 and last_int != 0:
    print(f"Last digit of {number} is -{last} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {last} and is 0")