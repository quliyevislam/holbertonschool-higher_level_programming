#!/usr/bin/python3

"""Unittests for max_integer function."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxIntegerFunction(unittest.TestCase):
    def test_list_of_integers(self):
        """Tests a list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty_list(self):
        """Tests an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_list_of_strings(self):
        """Tests a list of strings."""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")


if __name__ == "__main__":
    unittest.main()
