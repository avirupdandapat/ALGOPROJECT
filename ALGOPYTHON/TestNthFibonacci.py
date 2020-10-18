# Add, edit, or remove tests in this file.
# Treat it as your playground!
from __future__ import print_function

from ALGOPYTHON import NthFibonacci

# Add, edit, or remove tests in this file.
# Treat it as your playground!
import pytest
import unittest


class TestFibonacci(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(NthFibonacci.getNthFib(1), 0)

    def test_case_2(self):
        self.assertEqual(NthFibonacci.getNthFib(2), 1)

    def test_case_3(self):
        self.assertEqual(NthFibonacci.getNthFib(3), 1)

    def test_case_4(self):
        self.assertEqual(NthFibonacci.getNthFib(4), 2)

    def test_case_5(self):
        self.assertEqual(NthFibonacci.getNthFib(5), 3)

    def test_case_6(self):
        self.assertEqual(NthFibonacci.getNthFib(6), 5)

    def test_case_7(self):
        self.assertEqual(NthFibonacci.getNthFib(7), 8)

    def test_case_8(self):
        self.assertEqual(NthFibonacci.getNthFib(8), 13)

    def test_case_9(self):
        self.assertEqual(NthFibonacci.getNthFib(9), 21)

    def test_case_10(self):
        self.assertEqual(NthFibonacci.getNthFib(10), 34)

    def test_case_11(self):
        self.assertEqual(NthFibonacci.getNthFib(11), 55)

    def test_case_12(self):
        self.assertEqual(NthFibonacci.getNthFib(12), 89)

    def test_case_13(self):
        self.assertEqual(NthFibonacci.getNthFib(13), 144)

    def test_case_14(self):
        self.assertEqual(NthFibonacci.getNthFib(14), 233)

    def test_case_15(self):
        self.assertEqual(NthFibonacci.getNthFib(15), 377)

    def test_case_16(self):
        self.assertEqual(NthFibonacci.getNthFib(16), 610)

    def test_case_17(self):
        self.assertEqual(NthFibonacci.getNthFib(17), 987)

    def test_case_18(self):
        self.assertEqual(NthFibonacci.getNthFib(18), 1597)


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFibonacci)
    unittest.TextTestRunner(verbosity=2).run(suite)
