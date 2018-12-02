#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
# import subprocess
import sys
import StringIO


class TestNumSeq(unittest.TestCase):
    # def test_help(self):
    #     """ Running the program without arguments should show usage. """

    #     # Run the command `python ./echo.py -h` in a separate process, then
    #     # collect it's output.
    #     process = subprocess.Popen(
    #         ["python", "./echo.py", "-h"],
    #         stdout=subprocess.PIPE)
    #     stdout, _ = process.communicate()
    #     usage = open("./USAGE", "r").read()

    #     self.assertEqual(stdout, usage)

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

        print("Geometric numbers (square, triangle, cube)")
        for i in range(10):
            print ("{}: {} {} {}".format(i, square(i), triangle(i), cube(i)))


if __name__ == '__main__':
    unittest.main()
