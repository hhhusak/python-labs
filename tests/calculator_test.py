import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from functions.calculator_functions import perform_calculation

class TestCalculatorFunctions(unittest.TestCase):

    def testAdd(self):
        self.assertEqual(perform_calculation(1, '+', 2), 3)

    def testSubstract(self):
        self.assertEqual(perform_calculation(5, '-', 3), 2)

    def testMultiplication(self):
        self.assertEqual(perform_calculation(4, '*', 2), 8)

    def testDivision(self):
        self.assertEqual(perform_calculation(10, '/', 2), 5)

    def testExceptions(self):
        self.assertEqual(perform_calculation(10, '/', 0), "Помилка! Ділення на нуль.")