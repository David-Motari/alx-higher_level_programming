#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

lst_d = number % 10
if lst_d > 5:
    print(f"Last digit of {number} is {lst_d} and is greater than 5")
elif lst_d == 0:
    print(f"Last digit of {number} is {lst_d} and is 0")
elif lst_d < 6 and lst_d != 0:
    print(f"Last digit of {number} is {lst_d} and is less than 6 and not 0")
