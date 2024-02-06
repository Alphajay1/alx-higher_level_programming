#!/usr/bin/python3
"""
Contains the function append_write
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a UTF8 text file.
    
    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
