#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0
    if not my_list:
        print("")
        return (0)
    while y < x:
        try:
            print("{}".format(my_list[y]), end="")
            y = y + 1
        except IndexError:
            break
    print("")
    return (y)
