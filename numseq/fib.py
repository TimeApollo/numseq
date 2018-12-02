#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""fib module contains a function for fibonacci sequence."""


def fib(nth):
    """returns the nth number in fibonacci sequence"""
    first, second = 0, 1
    for _ in range(nth):
        first, second = second, first + second
    return first
