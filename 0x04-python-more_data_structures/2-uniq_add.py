#!/usr/bin/python3
def uniq_add(my_list=[]):
    """add unique integers of a list."""
    add_s = 0
    for j in set(my_list):
        add_s += j
    return add_s
