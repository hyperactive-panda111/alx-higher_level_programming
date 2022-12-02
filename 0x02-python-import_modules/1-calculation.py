#!/usr/bin/python3
if __name__ = "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(add(a, b)))
    print("{:d} - {:d} = {:d}".format(sub(a, b)))i
    print("{:d} * {:d} = {:d}".format(mul(a, b)))
    print("{:d} / {:d} = {:d}".format(div(a, b)))
