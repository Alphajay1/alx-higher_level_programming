#!/usr/bin/python3
"""Defining from_json_string function"""

import json


def from_json_string(my_string):
    """Returns an object (Python data structure) represented by JSON string"""
    return json.loads(my_string)
