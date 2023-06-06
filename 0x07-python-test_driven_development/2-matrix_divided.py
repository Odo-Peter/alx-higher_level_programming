#!/usr/bin/python3
"""
Module matrix_divide
This module contains a function that divides a matrix
"""


def matrix_divided(matrix, div):
    """
    Funciton that divides an array matrix by a given number
    Args:
        matrix: An array of two rows of equal size
        div: A integer/float that is greater than zero
    Returns:
        A new matrix with each element from `matrix`
        being divided by `div`
    Raises:
        TypeError: if `matrix` is not an array matrix
        TypeError: if the length of matrix[1] != length of (matrix[n])
        TypeError: if `div` is not a number
        ZeroDivisionError: if `div` is 0
    """
    error_str = "matrix must be a matrix (list of lists) of integers/floats"

    if len(matrix) < 2:
        raise TypeError(error_str)

    if not isinstance(matrix, list):
        raise TypeError(error_str)

    for items in matrix:
        for n in items:
            if not type(n) in (int, float):
                raise TypeError(error_str)

    for mat in matrix:
        if len(matrix[0]) != len(mat):
             raise TypeError("Each row of the matrix must have the same size")

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for item in matrix:
        new_matrix.append(list(item))
    val = 0
    count = 0
    while len(new_matrix) - 1 >= count:
        for idx, i in enumerate(new_matrix[count]):
            val = float("{:.2f}".format(i / div))
            new_matrix[count][idx] = val
        count += 1
    return (new_matrix)
