#!/usr/bin/python3

import sys

if __name__ == "__main__":
    for i in range(1, len(sys.argv)):
        print("{}".format(f"{i}: {sys.argv[i]}"))
