import unittest
from other.fizz_buzz.fizz_buzz import *


class FizzBuzzTests(unittest.TestCase):

    def test(self):
        self.assertEqual(fizz_buzz(5), ["1", "2", "Fizz", "4", "Buzz"])
        self.assertEqual(fizz_buzz(15),
                         ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14",
                          "FizzBuzz"])
