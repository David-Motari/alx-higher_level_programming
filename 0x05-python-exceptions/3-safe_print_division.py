#!/usr/bin/python3

def safe_print_division(a, b):
    """
        divides two integers and returns the result
        a: integer
        b: integer
        Return: a/b else None
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
