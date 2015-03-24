remove_hairs
===============================

.. image:: https://badge.fury.io/py/remove_hairs.png
    :target: http://badge.fury.io/py/remove_hairs

.. image:: https://pypip.in/d/remove_hairs/badge.png
        :target: https://pypi.python.org/pypi/remove_hairs


Function form removing characters from both sides of string.

Documentation
-------------

There is just one function ``remove_hairs()`` and one decorator
``remove_hairs_decorator()``.

remove_hairs()
++++++++++++++

This function is useful, when you have string and you need to remove some
characters from both sides of the string.

.. code-block:: python

    >>> from remove_hairs import remove_hairs
    >>> remove_hairs(",a-sd,-/")
    'a-sd'

By default, the function uses set of characters defined in ``.HAIRS``, which
is defined as ``/:;,- []<>()``. You can change that using ``hairs`` parameter:

.. code-block:: python

    >>> remove_hairs(" - a sd: --", " -")
    'a sd:'

remove_hairs_decorator()
++++++++++++++++++++++++

As the name say, ``remove_hairs_decorator()`` is just decorator for ``remove_hairs()``:

.. code-block:: python

    @remove_hairs_decorator
    def x():
        return ",a-sd,-/"

    assert x() == "a-sd"

Or with ``hairs`` parameter:

.. code-block:: python

    @remove_hairs_decorator(hairs=" -")
    def y():
        return " - a sd: --"

    assert y() == "a sd:"

Installation
------------

The code is hosted at `PYPI <https://pypi.python.org/pypi/remove_hairs>`_,
and you can easily install it using the following command:

.. code-block:: bash

    sudo pip install remove_hairs

Testing
-------

This project uses `py.test <http://pytest.org/latest/>`_ for testing. Just run
``py.test`` from the root of the project::

    $ py.test
    ============================= test session starts ==============================
    platform linux2 -- Python 2.7.6 -- py-1.4.26 -- pytest-2.6.4
    collected 2 items 

    tests/test_remove_hairs.py ..

    =========================== 2 passed in 0.02 seconds ===========================
