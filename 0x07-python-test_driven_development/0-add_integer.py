#!/usr/bin/python3
"""
Module 0-add_integer
This module houses a function that adds two numbers
"""


def add_integer(a, b=98):
    """ Function that adds two integer or floats
    Args:
        a: first number
        b: second number
    Returns:
        The added value of the two params
    Raises:
        TypeError: if a or b are not integer and/or float values
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return(a + b)
