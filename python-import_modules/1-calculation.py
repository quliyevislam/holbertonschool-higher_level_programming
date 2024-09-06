#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

a = 10
b = 5

print("{}".format(f"{a} + {b} = {add(a, b)}"))
print("{}".format(f"{a} - {b} = {sub(a, b)}"))
print("{}".format(f"{a} * {b} = {mul(a, b)}"))
print("{}".format(f"{a} / {b} = {div(a, b)}"))
