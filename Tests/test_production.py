'''
A file for tests for the production code.
'''
import unittest
from production import reverse_word

from test_production import *

class TestReverseWord(unittest.TestCase):

  def test_reverse_olleh(self):
    self.assertEqual(reverse_word("olleh"), "hello")

  def test_reverse_na(self):
    self.assertEqual(reverse_word(""), "")

  def test_reverse_numbers(self):
    self.assertEqual(reverse_word("12345"), "54321")



