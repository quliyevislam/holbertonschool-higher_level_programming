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
    if not isinstance(m_a, (list, np.ndarray)) or not isinstance(m_b, (list, np.ndarray)):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    
    try:
        return np.matmul(m_a, m_b)
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
    except TypeError:
        raise TypeError("Scalar operands are not allowed, use '*' instead")
