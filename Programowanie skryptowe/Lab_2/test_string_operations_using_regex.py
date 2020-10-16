import string_operations_using_regex
import unittest
from unittest import TestCase


class Test_RegEX(TestCase):

    def test_regex_word(self):
        self.assertEqual(string_operations_using_regex.logic('aaaaa'), '\tWyraz: aaaaa\n')
        self.assertEqual(string_operations_using_regex.logic('aaaaabbbbb'), '\tWyraz: aaaaabbbbb\n')

    #
    def test_regex_number(self):
        self.assertEqual(string_operations_using_regex.logic('423422'), '\tLiczba: 423422\n')

    def test_regex_combined(self):
        self.assertEqual(string_operations_using_regex.logic('a423422b'), '\tWyraz: a\n\tLiczba: 423422\n\tWyraz: b\n')
        self.assertEqual(string_operations_using_regex.logic('423422b'), '\tLiczba: 423422\n\tWyraz: b\n')
        self.assertEqual(string_operations_using_regex.logic('a4a'), '\tWyraz: a\n\tLiczba: 4\n\tWyraz: a\n')


if __name__ == '__main__':
    unittest.main()
