#!/usr/bin/python3
import json
"""This module contains from_json_string() function"""


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string

    Parameters
    ----------
        my_str : str
    Return
    ------
        str
            An object (Python data structure) represented by a JSON string

    """
    return json.loads(my_str)
