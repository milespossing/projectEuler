import unittest
import MathPackage.NumberOperations

class NumberOperationsTests(unittest.TestCase):
    def test_combiner(self):
        a = 250
        b = 430
        c = MathPackage.NumberOperations.combiner(a,b)
        self.assertEqual(c,250430,"Test")
