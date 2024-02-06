#!/usr/bin/python3
"""
Contains the write_file function
"""


def write_file(filename="", text=""):
    """Returns the number of characters written from "text" to "filename"."""
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
