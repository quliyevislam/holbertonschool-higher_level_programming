#!/usr/bin/python3

for i in range(90, 64, -1):

    if i % 2 == 0:
        i = i + 32

    print("{}".format(chr(i)), end="")

    if i % 2 == 0:
        i = i - 32
