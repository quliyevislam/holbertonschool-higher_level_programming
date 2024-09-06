#!/usr/bin/python3

p = print
r = range

[p("{}".format(f"{i:02}"), end=", " if i < 99 else "\n") for i in r(0, 100)]
