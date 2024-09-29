#!/usr/bin/python3
"""This module contains MyInt class"""


class MyInt(int):
    """
    This class overrides the `__eq__()` and `__ne__()` functions
    """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
