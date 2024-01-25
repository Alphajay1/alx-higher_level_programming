#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        rtn = fct(*args)
        return rtn
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
