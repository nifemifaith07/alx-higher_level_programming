#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    add = 0
    for c in argv[1:]:
        add += int(c)
    print("{:d}".format(add))
