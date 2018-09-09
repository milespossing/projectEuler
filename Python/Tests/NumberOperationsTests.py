from __future__ import division
import unittest
import MathPackage.NumberOperations

class NumberOperationsTests(unittest.TestCase):
    def test_combiner(self):
        a = 250
        b = 430
        c = MathPackage.NumberOperations.combiner(a,b)
        self.assertEqual(c,250430,"Test")

    def test_num2frac(self):
        a = 7
        b = 83
        c = a / b
        [aa,bb] = MathPackage.NumberOperations.Dec2Frac(c)
        self.assertEqual(a,aa)
        self.assertEqual(b,bb)

    def test_num2fracLarge(self):
        a = 8
        b = 3
        c = a / b
        [aa, bb] = MathPackage.NumberOperations.Dec2Frac(c)
        self.assertEqual(a, aa)
        self.assertEqual(b, bb)

    def test_digCount(self):
        a = 1234
        b = 1
        c = 45
        d = 100
        e = 12345678901234567
        self.assertEqual(4, MathPackage.NumberOperations.DigCount(a))
        self.assertEqual(1, MathPackage.NumberOperations.DigCount(b))
        self.assertEqual(2, MathPackage.NumberOperations.DigCount(c))
        self.assertEqual(3, MathPackage.NumberOperations.DigCount(d))
        self.assertEqual(17, MathPackage.NumberOperations.DigCount(e))
