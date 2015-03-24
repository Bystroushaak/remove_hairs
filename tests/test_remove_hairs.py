#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
import sys

import pytest

sys.path.append('src/')
from remove_hairs import remove_hairs
from remove_hairs import remove_hairs_decorator


# Functions & classes =========================================================
def test_remove_hairs():
    assert remove_hairs(",a-sd,-/") == "a-sd"

    assert remove_hairs(" - a sd. --", " -") == "a sd."

    assert remove_hairs(" -  --", " -") == ""

    assert remove_hairs(" -  --", "") == " -  --"

    assert remove_hairs("", "") == ""

    assert remove_hairs("", "-,.") == ""


def test_remove_hairs_decorator():
    @remove_hairs_decorator
    def x():
        return ",a-sd,-/"

    assert x() == "a-sd"

    @remove_hairs_decorator
    def x(a):
        return ",a-sd,-/"

    assert x(1) == "a-sd"

    @remove_hairs_decorator(hairs=" -")
    def y():
        return " - a sd. --"

    assert y() == "a sd."

    @remove_hairs_decorator(hairs=" -")
    def y(a):
        return " - a sd. --"

    assert y(1) == "a sd."
