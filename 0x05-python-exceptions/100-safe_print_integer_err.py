#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as err:
        import sys
        print("Exception: {}".format(err), file=sys.stderr)
        return False
    else:
        return True
