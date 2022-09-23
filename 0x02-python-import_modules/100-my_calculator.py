#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)
    a = int(argv[1])
    b = int(argv[3])
    ops = ["+", "-", "*", "/"]
    from calculator_1 import add, sub, mul, div
    func = [add, sub, mul, div]
    for i, o in enumerate(ops):
        if argv[2] == o:
            print("{} {} {} = {}".format(a, o, b, func[1](a, b)))
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        quit(1)
