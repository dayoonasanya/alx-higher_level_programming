#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    value = 0
    try:
        value = fct(*args)
        return value
    except Exception as info:
        sys.stderr.write("Exception: " + str(info) + "\n")
        return None
