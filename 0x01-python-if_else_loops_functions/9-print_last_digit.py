#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        number = number % 10
    else:
        rem = number * -1
        number = rem % 10
    print(number, end="")
    return number
