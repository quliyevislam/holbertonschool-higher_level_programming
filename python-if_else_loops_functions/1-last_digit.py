#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

LastDigit = number % 10 if number > 0 else (abs(number) % 10) * -1

prin = print

if LastDigit == 0:
    prin(f"Last digit of {number} is {LastDigit} and is 0")
elif LastDigit > 5:
    prin(f"Last digit of {number} is {LastDigit} and is greater than 5")
else:
    prin(f"Last digit of {number} is {LastDigit} and is less than 6 and not 0")
