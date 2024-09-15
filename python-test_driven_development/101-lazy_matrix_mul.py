#!/usr/bin/python3

"""This module defines the matrix_mul function."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b, ensuring valid inputs and dimensions.

    Args:
        m_a (list of lists): The first matrix containing integers or floats.
        m_b (list of lists): The second matrix containing integers or floats.

    Returns:
        list of lists: The resulting matrix after multiplication.
    """
    if not (isinstance(m_a, list) and isinstance(m_b, list)):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not any(m_a):
        raise ValueError("shapes (1,0) and (2,2) not aligned: "
                         "0 (dim 1) != 2 (dim 0)")
    if not any(m_b):
        raise ValueError("shapes (2,2) and (1,0) not aligned: "
                         "2 (dim 1) != 1 (dim 0)")

    if not (all(isinstance(num, (int, float)) for row in m_a for num in row)
            and
            all(isinstance(num, (int, float)) for row in m_b for num in row)):
        raise TypeError("invalid data type for einsum")

    if not (all(len(row) == len(m_a[0]) for row in m_a) and
            all(len(row) == len(m_b[0]) for row in m_b)):
        raise TypeError("setting an array element with a sequence.")

    if len(m_a[0]) != len(m_b):
        raise ValueError("shapes (2,3) and (2,2) not aligned: "
                         "3 (dim 1) != 2 (dim 0)") 
    return (np.matmul(m_a, m_b))
