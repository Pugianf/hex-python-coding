#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    last = last * (-1)
if last > 5:
    x = 'and is greater than 5'
elif last == 0:
    x = 'and is 0'
else:
    x = 'and is less than 6 and not 0'
print('Last digit of {} is {} '.format(number, last) + x)
