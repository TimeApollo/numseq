#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
import StringIO


class TestNumSeq(unittest.TestCase):
    """test cases defined in assignment to check modules"""

    def test_fib(self):
        """make sure fib prints expected fibonacci sequence"""
        from numseq.fib import fib

        saved_stdout = sys.stdout

        out = StringIO.StringIO()
        sys.stdout = out

        print("Fibonacci")
        for i in range(10):
            print("{}: {}".format(i, fib(i)))

        output = out.getvalue().strip()

        expected = open("./Fibonacci", "r").read()

        self.assertEquals(output, expected)
        sys.stdout = saved_stdout

    def test_geo(self):
        """varyifying geo functions from range 0 to 9"""
        from numseq.geo import square, triangle, cube

        saved_stdout = sys.stdout

        out = StringIO.StringIO()
        sys.stdout = out

        print("Geometric numbers (square, triangle, cube)")
        for i in range(10):
            print ("{}: {} {} {}".format(i, square(i), triangle(i), cube(i)))

        output = out.getvalue().strip()

        expected = open("./Geometric", "r").read()

        self.assertEquals(output, expected)
        sys.stdout = saved_stdout

    def test_prime(self):
        """varifying prime functions in prime module"""
        from numseq.prime import primes, is_prime

        saved_stdout = sys.stdout

        out = StringIO.StringIO()
        sys.stdout = out

        print ("Primes")
        prime_list = primes(1000)
        for p in prime_list[-10:]:
            print (p)
        print ("Is 999981 prime? {}".format(is_prime(999981)))
        print ("Is 999983 prime? {}".format(is_prime(999983)))

        output = out.getvalue().strip()

        expected = open("./Prime", "r").read()

        self.assertEquals(output, expected)
        sys.stdout = saved_stdout


if __name__ == '__main__':
    unittest.main()
