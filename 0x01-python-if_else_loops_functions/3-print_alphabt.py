#!/usr/bin/python3
for alpha in range(ord('a'), ord('z') + 1):
    if chr(alpha) != 'e' and chr(alpha) != 'q':
        print("{:c}".format(alpha), end='')
