#!/usr/bin/python3

up_alph = False
for i in range(25, -1, -1):
    xter = i + ord('A') if up_alph else i + ord('a')
    print("{:c}".format(xter), end="")
    up_alph = not up_alph
