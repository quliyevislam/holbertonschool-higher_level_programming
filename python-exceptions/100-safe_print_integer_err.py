#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """
    Prints an integer followed by a new line.

    Args:
        value: The value to print. Can be of any type.

    Returns:
        bool: True if the value is an integer and was printed successfully,
              False otherwise, with a generic error message printed to stderr.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        print("Exception: Invalid integer format", file=sys.stderr)
        return False
