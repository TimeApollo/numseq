#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Fib module contains a function for fibonacci sequence."""


def fib(nth):
    """Returns the nth number in fibonacci sequence."""
    first, second = 0, 1
    for _ in range(nth):
        first, second = second, first + second
    return first
