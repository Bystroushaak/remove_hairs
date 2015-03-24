#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
from functools import wraps


# Variables ===================================================================
HAIRS = "/:;,- []<>()"


# Functions & classes =========================================================
def remove_hairs(inp, hairs=HAIRS):
    """
    Remove "special" characters from beginning and the end of the `inp`. For
    example ``,a-sd,-/`` -> ``a-sd``.

    Args:
        inp (str): Input string.
        hairs (str): List of characters which should be removed. See
                     :attr:`HAIRS` for details.

    Returns:
        str: Cleaned string.
    """
    while inp and inp[-1] in hairs:
        inp = inp[:-1]

    while inp and inp[0] in hairs:
        inp = inp[1:]

    return inp


def remove_hairs_decorator(fn=None, hairs=HAIRS):
    """
    Parametrized decorator wrapping the :func:`remove_hairs` function.

    Args:
        hairs (str, default HAIRS): List of characters which should be removed.
                                    See :attr:`HAIRS` for details.
    """
    def decorator_wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            out = fn(*args, **kwargs)

            return remove_hairs(out, hairs)

        return decorator

    if fn:
        return decorator_wrapper(fn)

    return decorator_wrapper
