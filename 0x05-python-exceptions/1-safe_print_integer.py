#!/usr/bin/python3

def safe_print_integer(value):
    """
        prints an integer using "{:}".format()
        value: to be printed
        Returns true if successful else false
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
