#!/usr/bin/python3
"""This module contains append_after() method"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line
    """
    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
