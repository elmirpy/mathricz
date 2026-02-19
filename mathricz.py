#!usr/bin/env python3
# -*- coding: utf-8 -*-


"""Math utils"""


from __future__ import print_function

__author__ = "Elmir Santos"
__copyright__ = "Copyright 2026, Elmir Santos"
# __credits__ = []
__license__ = "Unlicense"
__version__ = "0.0.1"
__maintainer__ = "Elmir Santos"
# __email__ = ""
__status__ = "Development"


"""Functions of math proportion"""


def simple_proportion(a=None, b=None, c=None, d=None):
    """Simple proportion: a/b = c/d"""
    vals = [a, b, c, d]

    if vals.count(None) != 1:
        raise ValueError("Exactly one value must be None")

    try:
        if a is None: return b * c / d
        if b is None: return a * d / c
        if c is None: return a * d / b
        if d is None: return b * c / a
    except ZeroDivisionError:
        raise ValueError("Division by zero in proportion")



