#!/usr/bin/python3
"""
Defines the function read_file
"""


def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout:"""
    with open(filename, mode="r", encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
