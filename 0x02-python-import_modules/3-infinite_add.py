#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ret = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            ret += int(arg)
    print(ret)
