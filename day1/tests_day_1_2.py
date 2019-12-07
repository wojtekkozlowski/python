import unittest
from day1.day1_2 import *
from day1.day1_inputs import input_1_2


class Day12Tests(unittest.TestCase):

    def test_solution_1_2_1(self):
        self.assertEqual(solution_1_2_1([14]), 2)
        self.assertEqual(solution_1_2_1([1969]), 966)
        self.assertEqual(solution_1_2_1([100756]), 50346)
        self.assertEqual(solution_1_2_1(input_1_2), 5128195)

    def test_solution_1_2_2(self):
        self.assertEqual(solution_1_2_2([14]), 2)
        self.assertEqual(solution_1_2_2([1969]), 966)
        self.assertEqual(solution_1_2_2([100756]), 50346)

    def test_solution_1_2_3(self):
        self.assertEqual(solution_1_2_3([14]), 2)
        self.assertEqual(solution_1_2_3([1969]), 966)
        self.assertEqual(solution_1_2_3([100756]), 50346)
