#!/usr/bin/python3
def lookup(obj):
    """ Function returns list of available attributes
        and methods of object

    Args:
        obj: instance of the class

    Returns:
        List of attributes
    """

    return dir(obj)
