import unittest
from day1.day1_1 import *
from day1.day1_inputs import input_1_1


class Day11Tests(unittest.TestCase):

    def test_solution_1_1_1(self):
        self.assertEqual(solution_1_1_1([14]), 2)
        self.assertEqual(solution_1_1_1([12]), 2)
        self.assertEqual(solution_1_1_1([1969]), 654)
        self.assertEqual(solution_1_1_1([100756]), 33583)
        self.assertEqual(solution_1_1_1(input_1_1), 3420719)

    def test_solution_1_1_2(self):
        self.assertEqual(solution_1_1_2([14]), 2)
        self.assertEqual(solution_1_1_2([12]), 2)
        self.assertEqual(solution_1_1_2([1969]), 654)
        self.assertEqual(solution_1_1_2([100756]), 33583)
        self.assertEqual(solution_1_1_2(input_1_1), 3420719)

    def test_solution_1_1_3(self):
        self.assertEqual(solution_1_1_3([14]), 2)
        self.assertEqual(solution_1_1_3([12]), 2)
        self.assertEqual(solution_1_1_3([1969]), 654)
        self.assertEqual(solution_1_1_3([100756]), 33583)
        self.assertEqual(solution_1_1_3(input_1_1), 3420719)

    def test_solution_1_1_4(self):
        self.assertEqual(solution_1_1_4([14]), 2)
        self.assertEqual(solution_1_1_4([12]), 2)
        self.assertEqual(solution_1_1_4([1969]), 654)
        self.assertEqual(solution_1_1_4([100756]), 33583)
        self.assertEqual(solution_1_1_4(input_1_1), 3420719)
