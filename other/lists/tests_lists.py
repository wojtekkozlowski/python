import unittest
from other.lists.lists import *


class ListsTests(unittest.TestCase):

    def test_it(self):
        self.assertEqual(list_sum_it([1, 2, 3]), 6)

    def test_rec(self):
        self.assertEqual(list_sum_rec([1, 2, 3]), 6)

    def test_rec_pretty(self):
        self.assertEqual(list_sum_rec_prettified([1, 2, 3]), 6)
