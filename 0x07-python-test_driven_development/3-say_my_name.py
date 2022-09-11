#!/usr/bin/python3
"""
3-say_my_name
 prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    args: @first_name - first string name \
        @last_name - second string name.
    Raises: TypeError if either name is not string
    prints: statement.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
