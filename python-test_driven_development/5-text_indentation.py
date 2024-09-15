#!/usr/bin/python3

"""This module contains a function for text indentation."""


def text_indentation(text):
    """
    Prints text with two new lines after each of the following: `. ? :`

    Args:
        text (str): The text to be formatted.

    Raises:
        TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if '.' not in text and '?' not in text and ':' not in text:
        print(text, end="")
    prev = 0
    for i in range(len(text)):
        if text[i] in ('.', '?', ':') or i == len(text):
            print(text[prev:i + 1].strip(), end="\n\n")
            prev = i + 1
