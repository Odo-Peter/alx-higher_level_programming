#!/usr/bin/python3
"""
Module 3-say_my_name
This module contains a function that prints out the given args
"""


def say_my_name(first_name, last_name=""):
    """
    Function that conctenates the first and last name provided
    Args:
        first_name: A string passed as the first args
        last_name: A string passed as second args or empty string
    Returns:
        A concatenated string "first_name + last_name"
    Raises:
        TypeError: if any of the args are not of string values
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
