#!/usr/bin/python3
"""
py script that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds num that's greater than both left and right
    """
    if not list_of_integers:
        return None

    start = 0
    end = len(list_of_integers)-1

    if list_of_integers[start] > list_of_integers[start+1]:
        return list_of_integers[start]
    if list_of_integers[end] > list_of_integers[end-1]:
        return list_of_integers[end]
    middle = len(list_of_integers) // 2
    middle_val = list_of_integers[middle]

    if list_of_integers[middle - 1] < middle_val \
       and list_of_integers[middle + 1] < middle_val:
        return middle_val
    if middle_val < list_of_integers[middle - 1]:
        return find_peak(list_of_integers[start:middle + 1])
    elif middle_val < list_of_integers[middle + 1]:
        return find_peak(list_of_integers[middle:end + 1])
    else:
        return list_of_integers[start]
