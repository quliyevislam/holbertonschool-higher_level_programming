#!/usr/bin/python3

"""This module defines the matrix_mul function."""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b, ensuring valid inputs and dimensions.

    Args:
        m_a (list of lists): The first matrix containing integers or floats.
        m_b (list of lists): The second matrix containing integers or floats.

    Returns:
        list of lists: The resulting matrix after multiplication.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for i in m_a:
        if not isinstance(i, list):
            raise TypeError("m_a must be a list of lists")
    for i in m_b:
        if not isinstance(i, list):
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    if len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    for i in m_a:
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for i in m_b:
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    r_m_b = []
    m_m = []
    for column_i in range(len(m_b[0])):
        column = []
        for row_i in range(len(m_b)):
            column.append(m_b[row_i][column_i])
        r_m_b.append(column)
    for row_a in m_a:
        row = []
        for row_b in r_m_b:
            row.append(sum([a * b for a, b in zip(row_a, row_b)]))
        m_m.append(row)
    return m_m
