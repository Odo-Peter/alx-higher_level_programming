#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_len = len(my_list) - 1
    if (len(my_list) == 0):
        print("None")
    while list_len > -1:
        print("{:d}".format(my_list[list_len]))
        list_len -= 1
