#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""prime is a module to return primes and check for primes."""

import math


def primes(n):
    """list of all primes less than n"""
    primes = []
    if abs(n) != n:
        return primes
    if math.floor(n) != n:
        n = math.ceil(n)
    else:
        n = n
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes


def is_prime(m):
    """determines if integer is prime"""
    if math.floor(m) != m:
        raise Exception("Value must be an interger")
    if abs(m) != m:
        return False
    if m % 2 == 0:
        half = m/2
    else:
        half = (m + 1)/2
    for i in range(2, half):
        if m % i == 0:
            return False
    return True
