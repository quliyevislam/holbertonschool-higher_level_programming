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
    return np.matmul(m_a, m_b)
