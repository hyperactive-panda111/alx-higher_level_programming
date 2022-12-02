#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argv_cnt = len(argv)
    index = 1
    if argv_cnt is 0:
        print("{:d} arguments.".format(argv_cnt))
    elif argv_cnt is 1:
        print("{:d} argument:".format(argv_cnt))
        print("{:d}: {:s}".format(index, sys.argv[1]))
    else:
        print("{:d} arguments:".format(argv_cnt))
        while index <= argv_cnt:
            print("{:d}: {:s}".format(index, sys.argv[index]))
            index += 1
