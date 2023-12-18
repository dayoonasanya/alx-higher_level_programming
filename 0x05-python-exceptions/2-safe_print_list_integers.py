#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    y = 0
    err = 0
    if not my_list:
        print()
        return (0)
    while y < x:
        try:
            print("{:d}".format(my_list[y]), end="")
            y = y + 1
        except ValueError:
            y = y + 1
            err = err + 1
            pass
        except TypeError:
            y = y + 1
            err = err + 1
            pass
    print()
    return (y - err)
