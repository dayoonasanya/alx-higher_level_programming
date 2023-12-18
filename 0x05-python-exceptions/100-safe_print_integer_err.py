#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except Exception as info:
        sys.stderr.write("Exception: " + str(info) + "\n")
        return False
