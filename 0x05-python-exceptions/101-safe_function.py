#!/usr/bin/python3

def safe_function(fct, *args):
    """
     function that executes a function safely.
    """
    try:
        return fct(*args)
    except BaseException as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
